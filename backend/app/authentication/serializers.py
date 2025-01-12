from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db.utils import IntegrityError
# my user model
from core.models import User


class CustomRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    phone = serializers.CharField(required=False)
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
            user = adapter.new_user(request)
            user.email = validated_data.get('email')
            user.username = validated_data.get('username')
            user.phone = validated_data.get('phone')
            user.set_password(validated_data['password1'])
            user.save()
            setup_user_email(request, user, [])
            return user
        except IntegrityError as e:
            # Verify if the exception is cause by a duplicate email
            if 'duplicate key value violates unique constraint' in str(e):
                raise ValidationError(
                    {'email': 'A user with this email already exists.'})
            # raise other exceptions from database
            raise e
