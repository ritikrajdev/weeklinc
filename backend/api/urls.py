from django.shortcuts import redirect, reverse
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('schedules', views.ScheduleViewSet, 'schedule')
router.register('meets', views.MeetViewSet, 'meet')


urlpatterns = [
    path('auth/', include('api.auth.urls')),
    path('url/<str:username>/<str:schedule_name>/',
         views.MeetURLAPIView.as_view(), name='meet-url'),

    path('docs/', lambda *_: redirect(reverse('redoc'))),
    path('docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('docs/swagger/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),

    path('', include(router.urls))
]
