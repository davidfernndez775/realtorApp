from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.validators import EmailValidator
from authentication.validators import validate_us_phone_number
# my user model
from core.models import User


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

    def normalize_email(self, email):
        """Normalize the email domain."""
        local_part, domain_part = email.rsplit('@', 1)
        domain_part = domain_part.lower()  # Normalize domain to lowercase
        return f"{local_part}@{domain_part}"

    def save(self, request):
        validated_data = self.validated_data
        adapter = get_adapter()
        try:
            # create the user object
            user = adapter.new_user(request)
            user.email = self.normalize_email(validated_data.get('email'))
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
        fields = ['username', 'email', 'phone', 'first_name',
                  'last_name']  # Agrega otros campos si los necesitas

    def update(self, instance, validated_data):
        # Actualiza solo los campos enviados en validated_data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Guarda los cambios en la instancia del usuario
        try:
            instance.save()
        except DjangoValidationError as e:
            raise serializers.ValidationError({"error": list(e.messages)})
        return instance
