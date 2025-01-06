'''
Test for models
'''
# external libraries
from unittest.mock import patch
from decimal import Decimal

from django.test import TestCase
# to import model User defined in settings, use the method get_user_model
from django.contrib.auth import get_user_model
# import the other models
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

    def test_new_user_email_normalized(self):
        '''Test email is normalized for new users'''

        # normalize only the part before @
        sample_emails = [['test1@EXAMPLE.com', 'test1@example.com'],
                         ['Test2@Example.com', 'Test2@example.com'],
                         ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
                         ['test4@example.COM', 'test4@example.com'],]

        for email, expected in sample_emails:
            # for every email in create an user
            user = get_user_model().objects.create_user(email, 'sample123')

            self.assertEqual(user.email, expected)

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