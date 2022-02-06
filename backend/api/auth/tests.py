from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

User = get_user_model()

USER = {
    'username': 'tester',
    'email': 'tester@testing.com',
    'password': 'tester_testing'
}


class AuthAPITest(APITestCase):
    def test_create_user(self):
        # Not Logged in
        response = self.client.post(reverse('auth-user'), USER)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = USER.copy()
        del user['password']
        self.assertDictContainsSubset(user, response.data)

        # Logged In
        self.client.force_login(
            user=User.objects.get(username=USER['username']))
        response = self.client.post(reverse('auth-user'), USER)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_user(self):
        # Not Logged in
        response = self.client.get(reverse('auth-user'))
        self.assertIn(response.status_code, [
                      status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

        # Logged In
        user = User.objects.create_user(**USER)
        self.client.force_login(user=user)

        response = self.client.get(reverse('auth-user'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user = USER.copy()
        del user['password']
        self.assertDictContainsSubset(user, response.data)

    def test_token(self):
        user = User.objects.create_user(**USER)
        token = Token.objects.get(user=user)

        response = self.client.post(reverse('auth-token'), USER)
        self.assertEqual(response.data['token'], token.key)
