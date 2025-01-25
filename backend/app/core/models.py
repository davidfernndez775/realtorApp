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
from authentication.validators import validate_us_phone_number
from core.validators import validate_coordinates, validate_zip_code, validate_built


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
    phone = PhoneNumberField(blank=True, region="US", help_text="Enter a valid US phone number +1XXXXXXXXXX.", validators=[
                             validate_us_phone_number])
    is_active = models.BooleanField(default=True)
    # is_staff define if can access to Django Admin
    is_staff = models.BooleanField(default=False)
    # the fields password is in AbstractBaseUser and is_superuser
    # is in PermissionMixin

    # assign the UserManager to the class User
    objects = UserManager()

    # replace the authentication field username by the email field
    USERNAME_FIELD = 'email'


class RealEstateProperty(models.Model):
    # create the option's systems
    class PropertyType(models.TextChoices):
        SINGLE_FAMILY='Single Family'
        CONDO='Condo/Co-Op/Villa/Townhouse'
        MULTI_FAMILY='Multi-Family Income'
        RESIDENTIAL_LAND='Residential Land/Boat Docks'
        BUSSINESS='Land-Commercial/Business/Agricultural/Industrial'
        RESIDENTIAL_RENTAL='Residential Rental'
        COMMERCIAL='Commercial/Industrial'
        BUSSINESS_BROKERAGE='Business Brokerage'

    class PropertyStatus(models.TextChoices):
        FOR_SALE = 'for_sale', 'En venta'
        FOR_RENT = 'for_rent', 'En renta'

    class CountyList(models.TextChoices):
        BROWARD = 'Broward'
        CHARLOTTE = 'Charlotte'
        COLLIER = 'Collier'
        GLADES = 'Glades'
        HENDRY = 'Hendry'
        HIGHLANDS = 'Highlands'
        LEE = 'Lee'
        MARTIN = 'Martin'
        MIAMI_DADE = 'Miami Dade'
        MONROE = 'Monroe'
        OKEECHOBEE = 'Okeechobee'
        PALM_BEACH = 'Palm Beach'
        SAINT_LUCIE = 'Saint Lucie'

    # attributes
    title = models.CharField(max_length=255)
    lon = models.DecimalField(
        max_digits=8, decimal_places=5, help_text="Enter a valid coordinate, 1 to 3 digits before the comma and 5 after.", validators=[validate_coordinates])
    lat = models.DecimalField(max_digits=8, decimal_places=5, help_text="Enter a valid coordinate, 1 to 3 digits before the comma and 5 after.", validators=[
                              validate_coordinates])
    property_type = models.CharField(
        max_length=100,
        choices=PropertyType.choices,
    )
    address = models.TextField(max_length=255)
    county = models.CharField(max_length=20,
                              choices=CountyList.choices,)
    zip_code = models.IntegerField(validators=[
        validate_zip_code])
    for_rent_or_sale = models.CharField(
        max_length=100,
        choices=PropertyStatus.choices,
        default=PropertyStatus.choices[0]
    )
    price = models.IntegerField()
    beds = models.IntegerField(blank=True)
    full_baths = models.IntegerField(blank=True)
    half_baths = models.IntegerField(blank=True)
    square_ft = models.IntegerField(blank=True)
    water_front = models.BooleanField(default=False)
    built = models.IntegerField(blank=True, validators=[validate_built])
    description = models.TextField(blank=True, max_length=400)
    owner = models.CharField(max_length=50)
    phone_number = PhoneNumberField(blank=True, region="US", help_text="Enter a valid US phone number +1XXXXXXXXXX.", validators=[
        validate_us_phone_number])
    
    def __str__(self):
        return self.title


class Comments(models.Model):
    '''Comments from clients'''
    author = models.CharField(max_length=50)
    content = models.TextField(max_length=400)
    # flag to define if the comment is going to be show or not
    in_use = models.BooleanField()
    
    def __str__(self):
        return self.content
