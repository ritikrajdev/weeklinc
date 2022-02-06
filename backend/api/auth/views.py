from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from .permissions import AuthUserPermission
from .serializers import UserSerializer

User = get_user_model()


class AuthUserAPIView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [AuthUserPermission]

    def get_object(self):
        return User.objects.get(username=self.request.user.username)
