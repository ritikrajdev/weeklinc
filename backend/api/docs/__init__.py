"""
Doc Generation for api

Required Settings :-
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api.docs'
]

REST_FRAMEWORK = {
    ...
    'DEFAULT_SCHEMA_CLASS': 'api.docs.schemas.AutoSchema'
}


API_DOCS = {
    "title": "Descriptive title for the schema definition.",
    "description": "Longer descriptive text.",
    "version": "The version of the API.",
    "url": "canonical base URL for the schema.",
    "urlconf": "A string representing the import path to the URL conf that you want to generate an API schema.",
    "patterns": "List of url patterns to limit the schema introspection to."
}
"""
