'''
Database models
'''
import uuid
import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
# to handle phonenumbers
from phonenumber_field.modelfields import PhoneNumberField


def recipe_image_file_path(instance, filename):
    '''Generate a file path for new recipe image'''
    # take the extension from the name of the file
    ext= os.path.splitext(filename)[1]
    # assign a unique name and add the extension again
    filename = f'{uuid.uuid4()}{ext}'
    # return the full path
    return os.path.join('uploads', 'recipe', filename)


class UserManager(BaseUserManager):
    '''Manager for users'''

    # el metodo contiene la informacion minima necesaria para crear un usuario
    # se usa un valor por defecto para el password por si queremos usar
    # usuarios de prueba. Todas las modificaciones que hagamos en la clase User
    # van a pasar a traves de **extra_fields sin tener que modificar el UserManager
    def create_user(self, email, password=None, **extra_fields):
        '''Create, save and return a new user'''
        # se chequea que el email exista
        if not email:
            raise ValueError('User most have an email address')
        # se crea el usuario, notese que se normaliza el email, por si tiene mayusculas despues
        # de la @. normalize_email es un metodo de la clase BaseUserManager
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # el password se agrega despues de encriptado
        user.set_password(password)
        # se guarda en la base de datos
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        '''Create and return a new superuser'''
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    '''User in the system'''
    email = models.EmailField(max_length=255, unique=True)
    # 255 is CharField max_length
    name = models.CharField(max_length=255)
    phone = PhoneNumberField()
    is_active = models.BooleanField(default=True)
    # is_staff define if can access to Django Admin
    is_staff = models.BooleanField(default=False)
    # the fields password is in AbstractBaseUser and is_superuser
    # is in PermissionMixin


    # assign the UserManager to the class User
    objects = UserManager()

    # replace the authentication field username by the email field
    USERNAME_FIELD = 'email'