'''
Test for the authentication API
'''

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('authentication:rest_register')
# TOKEN_URL = reverse('user:token')
# ME_URL = reverse('user:me')


def create_user(**params):
    '''Create and return a new user'''
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    '''Test the public features of the user API'''

    def setUp(self):
        self.client = APIClient()

    def test_create_user_sucess(self):
        '''Test creating a user is successful'''
        # define the payload for the new user
        payload = {
            'email': 'test@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'username': 'Test Name',
            'phone': '+3057855689'
        }
        # send the http request for create the user
        res = self.client.post(CREATE_USER_URL, payload)

        # check the status code
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        # check the user has been created
        user = get_user_model().objects.get(email=payload['email'])
        # check the user password
        self.assertTrue(user.check_password(payload['password1']))
        # check that the password don't send back to the user in the response
        self.assertNotIn('password1', res.data)

    def test_user_with_email_exists_error(self):
        '''Test error returned if user with email exists'''
        # payload for database
        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'username': 'Test Name'
        }
        # payload for API because need two passwords fields
        payload2 = {
            'email': 'test@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'username': 'Test Name',
            'phone': '+3057855689'
        }
        # first create the user using the payload in database
        create_user(**payload)
        # then send a request to create another user with the same payload
        res = self.client.post(CREATE_USER_URL, payload2)
        # check that return a BAD_REQUEST
        self.assertEqual(
            res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        '''Test an error is returned if password less than 5 chars'''
        payload = {
            'email': 'test@example.com',
            'password1': 'pw',
            'password2': 'pw',
            'username': 'Test Name',
            'phone': '+3051874961'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        # check that return a BAD_REQUEST
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        # check that the user don't exists in database
        user_exists = get_user_model().objects.filter(
            email=payload['email']).exists()
        self.assertFalse(user_exists)

    # def test_invalid_phone_number(self):
    #     '''Test an error is returned if phone number is invalid'''
    #     # define the payload for the new user
    #     payload = {
    #         'email': 'test@example.com',
    #         'password1': 'testpass123',
    #         'password2': 'testpass123',
    #         'username': 'Test Name',
    #         'phone': 'phone not valid'
    #     }
    #     # send the http request for create the user
    #     res = self.client.post(CREATE_USER_URL, payload)

    #     # check the status code
    #     self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    #     # check that the user don't exists in database
    #     user_exists = get_user_model().objects.filter(
    #         email=payload['email']).exists()
    #     self.assertFalse(user_exists)
