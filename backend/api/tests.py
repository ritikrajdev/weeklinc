from django.shortcuts import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from .generics.test import USER, ModelAPITest, User
from .models import Meet, Schedule

SCHEDULE = {
    'name': 'sch'
}


class ScheduleTestCase(ModelAPITest, APITestCase):
    data = SCHEDULE
    path = reverse('schedule-list')


URL = 'https://example.com/'


class MeetURLTestCase(APITestCase):
    def setUp(self) -> None:
        user = {'password': 'testing'}
        user.update(USER)

        user = User.objects.create_user(**user)
        user.save()

        schedule = {'user': user}
        schedule.update(SCHEDULE)

        schedule = Schedule.objects.create(**schedule)
        schedule.save()

        now = timezone.now()
        thirty_minutes = timezone.timedelta(minutes=30)

        meet = {
            'name': 'mt',
            'schedule': schedule,
            'start_datetime': now - thirty_minutes,
            'end_datetime': now + thirty_minutes,
            'url': URL
        }
        meet = Meet.objects.create(**meet)
        meet.save()

    def test_meet_url(self):
        response = self.client.get(reverse('meet-url', kwargs={
            'username': USER['username'],
            'schedule_name': SCHEDULE['name']
        }))

        self.assertDictEqual(response.data, {'url': URL})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(reverse('meet-url', kwargs={
            'username': USER['username'] + 'x',
            'schedule_name': SCHEDULE['name']
        }))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get(reverse('meet-url', kwargs={
            'username': USER['username'],
            'schedule_name': SCHEDULE['name'] + 'y'
        }))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
