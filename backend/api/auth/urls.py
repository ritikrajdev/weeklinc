from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import AuthUserAPIView

urlpatterns = [
    path('user/', AuthUserAPIView.as_view(), name='auth-user'),
    path('token/', obtain_auth_token, name='auth-token'),
    path('jwt-token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('jwt-token/refresh', TokenRefreshView.as_view(), name='jwt-token-refresh')
]
