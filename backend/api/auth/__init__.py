"""
Authentication for api

Required Settings :-
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'api.auth',
    ...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ],
    ...
}

Now just include "api.auth.urls" wherever you may want.
"""
