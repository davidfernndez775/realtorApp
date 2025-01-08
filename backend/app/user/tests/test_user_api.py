'''
Test for the user API
'''

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')
ME_URL = reverse('user:me')


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
            'password': 'testpass123',
            'name': 'Test Name'
        }
        # send the http request for create the user
        res = self.client.post(CREATE_USER_URL, payload)

        # check the status code
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        # check the user has been created
        user = get_user_model().objects.get(email=payload['email'])
        # check the user password
        self.assertTrue(user.check_password(payload['password']))
        # check that the password don't send back to the user in the response
        self.assertNotIn('password', res.data)

    def test_user_with_email_exists_error(self):
        '''Test error returned if user with email exists'''
        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'name': 'Test Name'
        }
        # first create the user using the payload in database
        create_user(**payload)
        # then send a request to create another user with the same payload
        res = self.client.post(CREATE_USER_URL, payload)
        # check that return a BAD_REQUEST
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        '''Test an error is returned if password less than 5 chars'''
        payload = {
            'email': 'test@example.com',
            'password': 'pw',
            'name': 'Test Name'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        # check that return a BAD_REQUEST
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        # check that the user don't exists in database
        user_exists = get_user_model().objects.filter(
            email=payload['email']).exists()
        self.assertFalse(user_exists)
