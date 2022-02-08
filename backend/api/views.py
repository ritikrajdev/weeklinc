from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Meet, Schedule
from .serializers import MeetSerializer, MeetURLSerializer, ScheduleSerializer
from .decorators import apply_filters


class ScheduleViewSet(ModelViewSet):
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ['name']
    filterset_fields = ordering_fields

    @apply_filters
    def get_queryset(self):
        return self.request.user.schedules.all()


class MeetViewSet(ModelViewSet):
    serializer_class = MeetSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ['name', 'start_datetime', 'end_datetime']
    filterset_fields = ordering_fields + ['schedule']

    @apply_filters
    def get_queryset(self):
        return Meet.objects.filter(schedule__in=self.request.user.schedules.all())


class MeetURLAPIView(APIView):
    serializer_class = MeetURLSerializer

    def get(self, request, username, schedule_name, format=None):
        """
        Obtain meet ongoing link from username and schedule_name.
        URL will be an empty string if no meeting exists at that time.
        """
        User = get_user_model()
        user = get_object_or_404(User, username=username)
        schedule = get_object_or_404(Schedule, name=schedule_name, user=user)

        now = timezone.now()

        url = ''
        try:
            meet = schedule.meets.get(
                start_datetime__lte=now, end_datetime__gt=now)
            url = meet.url
        except Meet.DoesNotExist:
            pass
        return Response({'url': url})
