"""
Generic Test Generator for Models

inherit from (APITestCase, ModelAPITestCase)

override test_<view.method> for any model to skip or create any custom test
"""
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()
USER = {
    'username': 'tester',
    'email': 'tester@testing.com',
}


class ModelAPITest:
    """
    Generic Test Generator for Models
    inherit from (APITestCase, ModelAPITestCase)
    override test_<view.method> for any model to skip or create any custom test
    """
    data: dict
    path: str

    # From APITestCase
    # client: APIClient

    def setUp(self):
        user = {'password': 'tester_testing'}
        user.update(USER)
        User.objects.create_user(**user)

    def test_create(self):
        data = self.__class__.data
        path = self.__class__.path

        self.client.force_login(user=User.objects.get(**USER))

        response = self.client.post(path, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertDictContainsSubset(data, response.data)

    def test_delete(self):
        data = self.__class__.data
        path = self.__class__.path

        self.client.force_login(user=User.objects.get(**USER))

        # Creation
        response = self.client.post(path, data)

        path += f'' if path.endswith('/') else '/'
        path += str(response.data["id"])

        response = self.client.delete(path)
        self.assertIn(
            response.status_code,
            [status.HTTP_204_NO_CONTENT, status.HTTP_301_MOVED_PERMANENTLY]
        )

    def test_retrieve(self):
        data = self.__class__.data
        path = self.__class__.path

        self.client.force_login(user=User.objects.get(**USER))

        response = self.client.get(path)
        self.assertEqual([], response.data)

        response = self.client.post(path, data)
        cmp_with = [response.data]
        response = self.client.get(path)

        self.assertEqual(cmp_with, response.data)
