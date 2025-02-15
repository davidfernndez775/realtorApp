'''
Serializers for users
'''

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from authentication.validators import validate_us_phone_number
from dj_rest_auth.registration.serializers import RegisterSerializer

from django.contrib.auth.password_validation import validate_password
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.validators import EmailValidator

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models import User, FavoriteProperty


class CustomRegisterSerializer(RegisterSerializer):
    '''Serializer for register an user'''
    phone = serializers.CharField(required=False, validators=[
                                  validate_us_phone_number])

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'phone': self.validated_data.get('phone', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        try:
            self.cleaned_data = self.get_cleaned_data()
            user = adapter.save_user(request, user, self, commit=False)
            user.phone = self.cleaned_data['phone']       # add the phone
            if "password1" in self.cleaned_data:
                try:
                    adapter.clean_password(
                        self.cleaned_data['password1'], user=user)
                except DjangoValidationError as exc:
                    raise serializers.ValidationError(
                        detail=serializers.as_serializer_error(exc)
                    )
            user.save()
            self.custom_signup(request, user)
            setup_user_email(request, user, [])
            return user
        except IntegrityError as e:
            # Verify if the exception is caused by a duplicate email
            if 'duplicate key value violates unique constraint "core_user_email_key"' in str(e):
                raise ValidationError(
                    {'email': 'A user with this email already exists.'})
            raise e


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    '''Serializer for user detail view'''
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
        # update the fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)  # hash the password

        # save the changes in user instance
        try:
            instance.save()
        except DjangoValidationError as e:
            raise serializers.ValidationError({"error": list(e.messages)})
        return instance


class FavoritePropertySerializer(serializers.ModelSerializer):
    '''Serializer for favorite real estate properties'''

    class Meta:
        model = FavoriteProperty
        fields = ['id', 'user', 'property', 'added_at']
        read_only_fields =['id', 'added_at']