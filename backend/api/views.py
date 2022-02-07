from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .serializers import MeetSerializer, ScheduleSerializer
from .models import Meet


class ScheduleViewSet(ModelViewSet):
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.schedules.all()


class MeetViewSet(ModelViewSet):
    serializer_class = MeetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Meet.objects.filter(schedule__in=self.request.user.schedules.all())
