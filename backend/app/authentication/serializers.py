from rest_framework import serializers
# allauth
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
# validators
from django.core.validators import EmailValidator
from django.contrib.auth.password_validation import validate_password
from authentication.validators import validate_us_phone_number
# errors
from rest_framework.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError as DjangoValidationError
# my user model
from core.models import User


def normalize_email(email):
    """Normalize the email domain."""
    local_part, domain_part = email.rsplit('@', 1)
    domain_part = domain_part.lower()  # Normalize domain to lowercase
    return f"{local_part}@{domain_part}"


class CustomRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, validators=[
                                   EmailValidator(message="Invalid email format.")])
    username = serializers.CharField(required=True)
    phone = serializers.CharField(required=False, validators=[
                                  validate_us_phone_number])
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'phone')

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords don't match.")
        return data

    def save(self, request):
        validated_data = self.validated_data
        adapter = get_adapter()
        try:
            # create the user object
            user = adapter.new_user(request)
            user.email = normalize_email(validated_data.get('email'))
            user.username = validated_data.get('username')
            user.phone = validated_data.get('phone')
            # validate password
            try:
                validate_password(validated_data['password1'], user)
            except DjangoValidationError as e:
                raise serializers.ValidationError(
                    {'password1': list(e.messages)})
            user.set_password(validated_data['password1'])
            user.save()
            setup_user_email(request, user, [])
            return user
        except IntegrityError as e:
            # Verify if the exception is caused by a duplicate email
            if 'duplicate key value violates unique constraint "core_user_email_key"' in str(e):
                raise ValidationError(
                    {'email': 'A user with this email already exists.'})
            # Verify if the exception is caused by a duplicate username
            if 'duplicate key value violates unique constraint "core_user_username_36e4f7f7_uniq"' in str(e):
                raise ValidationError(
                    {'username': 'A user with this username already exists.'})
            raise serializers.ValidationError(
                {"error": "A database error occurred. Please try again."})
            # raise other exceptions from database
            raise e
        except Exception as e:
            # Catch unexpected errors and raise a 400 response
            raise serializers.ValidationError({"error": str(e)})


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[EmailValidator(message="Invalid email format.")]
    )
    phone = serializers.CharField(
        required=False, validators=[validate_us_phone_number]
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8}
        }

    def update(self, instance, validated_data):
        # take out the password from validated_data
        password = validated_data.pop('password', None)
        email = validated_data.pop('email', None)
        # update the fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)  # hash the password
        instance.email = normalize_email(email)

        # save the changes in user instance
        try:
            instance.save()
        except DjangoValidationError as e:
            raise serializers.ValidationError({"error": list(e.messages)})
        return instance
