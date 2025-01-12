'''
Tests for the Django admin modifications
'''
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    '''Tests for Django admin'''

    # define a method to create two users
    def setUp(self):
        '''Create user and client'''
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            username='Test User'
        )

    def test_users_list(self):
        '''Test that users are listed on page'''
        url = reverse(
            'admin:core_user_changelist')   # url to return the list of users
        res = self.client.get(url)

        self.assertContains(res, self.user.username)
        self.assertContains(res, self.user.email)

    # as forcelogin with admin user, now check the access to the edit and
    # create pages

    def test_edit_user_page(self):
        '''Test the edit user page works'''
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        '''Test the create user page works'''
        # pagina que va a la creacion de un usuario
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
