"""
Api Handling

Required Settings :-
TIME_INPUT_FORMATS = [...]
DATE_INPUT_FORMATS = [...]
DATETIME_INPUT_FORMATS = [...]

# For filtering
INSTALLED_APPS = [
    ...
    'api',
    'django_filters'
]

REST_FRAMEWORK = {
    ...
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ],
}


Refer - https://docs.djangoproject.com/en/4.0/ref/settings/#datetime-input-formats
Refer - https://docs.djangoproject.com/en/4.0/ref/settings/#time-input-formats
Refer - https://docs.djangoproject.com/en/4.0/ref/settings/#date-input-formats
"""
