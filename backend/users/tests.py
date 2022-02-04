from django.test import TestCase
from django.contrib.auth.hashers import check_password

from .models import User


USER = {
    'username': 'tester',
    'email': 'tester@testing.com',
    'password': 'tester_testing'
}


class UserTest(TestCase):
    def setUp(self):
        User.objects.create_user(**USER)

    def test_email(self):
        tester = User.objects.get(username=USER['username'])
        self.assertEqual(tester.email, USER['email'])

    def test_password_not_plain_text(self):
        tester = User.objects.get(username=USER['username'])
        self.assertNotEqual(tester.password, USER['password'])

    def test_password_hashed(self):
        tester = User.objects.get(username=USER['username'])
        self.assertTrue(check_password(USER['password'], tester.password))
