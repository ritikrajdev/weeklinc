from django.shortcuts import reverse
from rest_framework.test import APITestCase

from .generics.test import ModelAPITest


class ScheduleTestCase(ModelAPITest, APITestCase):
    data = {
        'name': 'sch'
    }
    path = reverse('schedule-list')
