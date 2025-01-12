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
from phonenumber_field.phonenumber import PhoneNumber


def recipe_image_file_path(instance, filename):
    '''Generate a file path for new recipe image'''
    # take the extension from the name of the file
    ext = os.path.splitext(filename)[1]
    # assign a unique name and add the extension again
    filename = f'{uuid.uuid4()}{ext}'
    # return the full path
    return os.path.join('uploads', 'recipe', filename)


class UserManager(BaseUserManager):
    '''Manager for users'''

    # this method contains the less info needed to create an user
    # I use a default value for password if I can make test users
    # All changes in the class User are going throw **extrafields without modify
    # the UserManager
    def create_user(self, email, password=None, **extra_fields):
        '''Create, save and return a new user'''
        # check that email exists
        if not email:
            raise ValueError('User most have an email address')
        # # convert the phone from string to PhoneNumber
        # phone=PhoneNumber.from_string(phone)
        # create the user and normalize the email after the @,
        # normalize_email is a method of the class BaseUserManager
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # the password is added after encripted
        user.set_password(password)
        # save the user in database
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
    username = models.CharField(max_length=255, unique=True)
    phone = PhoneNumberField(blank=True)
    is_active = models.BooleanField(default=True)
    # is_staff define if can access to Django Admin
    is_staff = models.BooleanField(default=False)
    # the fields password is in AbstractBaseUser and is_superuser
    # is in PermissionMixin

    # assign the UserManager to the class User
    objects = UserManager()

    # replace the authentication field username by the email field
    USERNAME_FIELD = 'email'
