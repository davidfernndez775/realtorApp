'''
Serializers for the user API View
'''
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext as _
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    '''Serializer for the user object'''

    class Meta:
        model = get_user_model()
        # define the fields that can be modified by the user
        fields = ['email', 'password', 'name', 'phone']
        # the key write_only is added to avoid that the password be return
        # in the response to the user, is more safety
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        '''Create and return a user with encryted password'''
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        '''Update and return user'''
        # first take out the password from validated_data and save it in a variable
        # this is because the update method don't pass the password throw the hashing process
        # must do it manually because the password get update as plain text
        password = validated_data.pop('password', None)
        # call the method update from Django
        user = super().update(instance, validated_data)
        # check if there is a password
        if password:
            # if the user send the password, I hash it and save it
            user.set_password(password)
            user.save()
        # return the updated user
        return user
