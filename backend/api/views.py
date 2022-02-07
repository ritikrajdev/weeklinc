from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwner
from .serializers import MeetSerializer, ScheduleSerializer
from .models import Meet


class ScheduleViewSet(ModelViewSet):
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.schedules.all()


class MeetViewSet(ModelViewSet):
    queryset = Meet.objects.all()
    serializer_class = MeetSerializer
    permission_classes = [IsAuthenticated, IsOwner]
