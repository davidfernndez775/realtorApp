'''
Test for the authentication API
'''

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core import mail

from rest_framework.test import APIClient
from rest_framework import status

from allauth.account.utils import send_email_confirmation
from allauth.account.models import EmailAddress

REGISTER_URL = reverse('authentication:rest_register')
LOGIN_URL = reverse('authentication:rest_login')
USER_URL = reverse('authentication:rest_user_details')
LOGOUT_URL = reverse('authentication:rest_logout')


def create_user(**params):
    '''Create and return a new user'''
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    '''Test the public features of the user API'''

    def setUp(self):
        self.client = APIClient()

    # *TESTS FOR REGISTER ENDPOINT

    def test_create_user_sucess(self):
        '''Test creating an user is successful'''
        # define the payload for the new user
        payload = {
            'email': 'test@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'username': 'Test Name',
            'phone': '+13057855689'
        }
        # send the http request for create the user
        res = self.client.post(REGISTER_URL, payload)

        # check the status code
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        # check the user has been created
        user = get_user_model().objects.get(email=payload['email'])
        # check the user password
        self.assertTrue(user.check_password(payload['password1']))
        # check that the password don't send back to the user in the response
        self.assertNotIn('password1', res.data)
        # check that an access token is receive
        self.assertIn('key', res.data)

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
            'phone': '+13057855689'
        }
        # first create the user using the payload in database
        create_user(**payload)
        # then send a request to create another user with the same payload
        res = self.client.post(REGISTER_URL, payload2)
        # check that return a BAD_REQUEST
        self.assertEqual(
            res.status_code, status.HTTP_400_BAD_REQUEST)
        # check that an access token is not receive
        self.assertNotIn('key', res.data)

    def test_user_with_username_exists_error(self):
        '''Test error returned if user with username exists'''
        # payload for database
        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'username': 'Test Name'
        }
        # payload for API because need two passwords fields
        payload2 = {
            'email': 'test2@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'username': 'Test Name',
            'phone': '+13057855689'
        }
        # first create the user using the payload in database
        create_user(**payload)
        # then send a request to create another user with the same payload
        res = self.client.post(REGISTER_URL, payload2)
        # check that return a BAD_REQUEST
        self.assertEqual(
            res.status_code, status.HTTP_400_BAD_REQUEST)
        # check that an access token is not receive
        self.assertNotIn('key', res.data)

    def test_new_user_email_normalized(self):
        '''Test email is normalized throw the API'''
        # normalize all the email
        sample_emails = [['test1@EXAMPLE.com', 'test1@example.com'],
                         ['Test2@Example.com', 'test2@example.com'],
                         ['TEST3@EXAMPLE.COM', 'test3@example.com'],
                         ['test4@example.COM', 'test4@example.com'],]
        count = 0
        for email, expected in sample_emails:
            # for every email in create an user
            payload = {
                'email': email,
                'password1': 'testpass123',
                'password2': 'testpass123',
                'username': f'Test Name{count}',
                'phone': '+13057855689'
            }
            res = self.client.post(REGISTER_URL, payload)
            count += 1
            #     # Inspecciona los datos almacenados
            # user = get_user_model().objects.filter(email__iexact=expected).first()
            # print(f"Expected: {expected}, Stored: {user.email if user else 'No user found'}")
            # check there is an user in database with an email equal to the expected
            user_exists = get_user_model().objects.filter(email=expected).exists()
            self.assertTrue(user_exists)
            # check that an access token is receive for each user
            self.assertIn('key', res.data)

    def test_password_too_short_error(self):
        '''Test an error is returned if password less than 5 chars'''
        payload = {
            'email': 'test@example.com',
            'password1': 'pw',
            'password2': 'pw',
            'username': 'Test Name',
            'phone': '+13051874961'
        }
        res = self.client.post(REGISTER_URL, payload)
        # check that return a BAD_REQUEST
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        # check that an access token is not receive
        self.assertNotIn('key', res.data)
        # check that the user don't exists in database
        user_exists = get_user_model().objects.filter(
            email=payload['email']).exists()
        self.assertFalse(user_exists)

    def test_invalid_phone_number(self):
        '''Test an error is returned if phone number is invalid'''
        # define the payload for the new user
        payload = {
            'email': 'test@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'username': 'Test Name',
            'phone': 'phone not valid'
        }
        # send the http request for create the user
        res = self.client.post(REGISTER_URL, payload)

        # check the status code
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        # check that an access token is not receive
        self.assertNotIn('key', res.data)
        # check that the user don't exists in database
        user_exists = get_user_model().objects.filter(
            email=payload['email']).exists()
        self.assertFalse(user_exists)

    # *TESTS FOR LOGIN ENDPOINT

    def test_login_user_sucess(self):
        '''Test login an user is successful'''
        # define the payload for the user
        payload = {
            'email': 'test@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'username': 'Test Name',
        }
        # create the user in database throw the endpoint
        res = self.client.post(REGISTER_URL, payload)
        # print("Response data:", res.data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        # email verification process manualy becuase in tests is not implemented
        # get the created user
        user = get_user_model().objects.get(email=payload["email"])
        email_address = EmailAddress.objects.get(user=user, email=user.email)

        # mark the email as verified
        email_address.verified = True
        email_address.save()

        # data for login
        login_payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'username': 'Test Name',
        }

        # send the http request for login the user
        res = self.client.post(LOGIN_URL, login_payload)
        # check the status code
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # check that an access token is receive
        self.assertIn('key', res.data)

    def test_login_user_fail_with_bad_credentials(self):
        '''Test returns an error if credentials invalid'''
        # create the user
        create_user(email='test@example.com', password='goodpass')
        # create the payload with wrong password
        payload = {'email': 'test@example.com', 'password': 'badpass'}
        # send the http request for login the user
        res = self.client.post(LOGIN_URL, payload)
        # check that an access token is not receive
        self.assertNotIn('key', res.data)
        # check the status code
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    # *TESTS FOR USER ENDPOINT

    def test_retrieve_user_unauthorized(self):
        '''Test authentication is required for users'''
        res = self.client.get(USER_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserApiTests(TestCase):
    '''Test API requests that require authentication'''

    def setUp(self):
        # define and authenticate the user
        self.user = create_user(
            email='test@example.com',
            password='testpass123',
            username='Test Name',
            phone='+13051874961'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    # *TESTS FOR USER ENDPOINT
    def test_retrieve_profile_success(self):
        '''Test retrieving profile for logged in user'''
        # get the authenticated user profile
        res = self.client.get(USER_URL)
        # check the status
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # compare the email in the response with the email from setUp
        self.assertEqual(res.data['email'], self.user.email)

    def test_post_method_in_user_endpoint_not_allowed(self):
        '''Test POST is not allowed for the me endpoint'''
        # send a POST request
        res = self.client.post(USER_URL, {})
        # check the status
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_profile_with_PATCH(self):
        '''Test updating the user profile for the authenticated user using PATCH'''
        # update the data
        payload = {
            'email': 'testUpdate@example.com',
            'password': 'testpasswordUpdate',
            'username': 'Test Name Updated',
            'phone': '+12025550123',
        }
        # send the http request
        res = self.client.patch(USER_URL, payload)
        # print(res.content)
        # update the user from database
        self.user.refresh_from_db()
        # check the status
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # check the payload of the request and data from database
        self.assertEqual(self.user.username, payload['username'])
        self.assertEqual(self.user.email, payload['email'])
        self.assertEqual(self.user.phone, payload['phone'])
        self.assertTrue(self.user.check_password(payload['password']))

    def test_update_user_profile_with_PUT(self):
        '''Test updating the user profile for the authenticated user using PUT'''
        # update the data
        payload = {
            'email': 'testUpdate@example.com',
            'password': 'testpasswordUpdate',
            'username': 'Test Name Updated',
            'phone': '+12025550123'
        }
        # send the http request
        res = self.client.put(USER_URL, payload)
        # print(res.content)
        # update the user from database
        self.user.refresh_from_db()
        # check the status
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # check the payload of the request and data from database
        self.assertEqual(self.user.username, payload['username'])
        self.assertEqual(self.user.email, payload['email'])
        self.assertEqual(self.user.phone, payload['phone'])
        self.assertTrue(self.user.check_password(payload['password']))

    # *TESTS FOR LOGOUT ENDPOINT

    def test_token_delete_when_logout(self):
        '''Test token delete when logout'''
        # send the http request for login the user
        res = self.client.post(LOGOUT_URL, {})
        # check that an access token is not receive
        self.assertNotIn('key', res.data)
