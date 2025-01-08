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
        fields = ['email', 'password', 'name']
        # the key write_only is added to avoid that the password be return
        # in the response to the user, is more safety
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        '''Create and return a user with encryted password'''
        return get_user_model().objects.create_user(**validated_data)

    # def update(self, instance, validated_data):
    #     '''Update and return user'''
    #     # primero tomamos el password del validated_data y lo guardamos en una variable
    #     # y lo borramos del validated_data, esto es porque el metodo update no pasa
    #     # el password por el proceso de hashing, por tanto debemos hacerlo manualmente
    #     # porque sino el password se actualiza como texto plano
    #     password = validated_data.pop('password', None)
    #     # invocamos el metodo update de Django para que haga el trabajo
    #     user = super().update(instance, validated_data)
    #     # chequeamos si hay un password
    #     if password:
    #         # si el usuario envio el password, lo pasamos por el hash y lo guardamos
    #         user.set_password(password)
    #         user.save()
    #     # retornamos el usuario actualizado
    #     return user