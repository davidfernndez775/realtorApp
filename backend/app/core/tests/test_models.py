'''
Test for models
'''

from unittest.mock import patch
from decimal import Decimal

from django.test import TestCase
from django.core.exceptions import ValidationError
# to import model User defined in settings, use the method get_user_model
from django.contrib.auth import get_user_model

from core import models

# method that call the method inside the model


def create_user(email='user@example.com', password='testpass123'):
    '''Create and return a new user'''
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    '''Test models'''

    def test_create_user_with_email_successful(self):
        '''Test creating a user with an email is successful'''
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_without_email_raises_error(self):
        '''Test that creating a user without an email raises a ValueError'''
        # if the email is blank, return ValueError
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        '''Test creating a superuser'''
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_user_with_invalid_phone(self):
        """Test creating a user with an invalid phone number"""
        user = get_user_model()(
            email='test@example.com',
            username="testuser",
            phone='827428',  # invalid number
        )
        with self.assertRaises(ValidationError):
            user.full_clean()  # execute the model's validation
            user.save()
