from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('schedules', views.ScheduleViewSet, 'schedule')
router.register('meets', views.MeetViewSet, 'meet')


urlpatterns = [
    path('auth/', include('api.auth.urls')),
    path('docs/', include('api.docs.urls')),
    path('url/<str:username>/<str:schedule_name>/',
         views.meet_url, name='meet-url'),
    path('', include(router.urls))
]
