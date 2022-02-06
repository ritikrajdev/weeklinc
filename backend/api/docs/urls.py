from django.urls import path

from . import views

urlpatterns = [
    path('schema/', views.schema_view, name='schema'),
    path('redoc/', views.redoc, name='redoc'),
    path('swagger/', views.swagger, name='swagger')
]
