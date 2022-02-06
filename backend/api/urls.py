from django.urls import path, include

urlpatterns = [
    path('auth/', include('api.auth.urls')),
    path('docs/', include('api.docs.urls')),
]
