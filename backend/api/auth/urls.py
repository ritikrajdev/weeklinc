from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import AuthUserAPIView

urlpatterns = [
    path('user/', AuthUserAPIView.as_view(), name='auth-user'),
    path('token/', obtain_auth_token, name='auth-token')
]
