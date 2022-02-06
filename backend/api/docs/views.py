from django.conf import settings
from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from django.http import JsonResponse
from rest_framework.schemas.openapi import SchemaGenerator

API_DOCS = {'title': _('API Docs')}

try:
    API_DOCS.update(settings.API_DOCS)
except AttributeError:
    pass


def schema_view(_):
    schema = SchemaGenerator(**API_DOCS).get_schema()
    return JsonResponse(schema)


redoc = TemplateView.as_view(
    template_name='api/docs/redoc.html', extra_context={'schema_url': 'schema'})

swagger = TemplateView.as_view(
    template_name='api/docs/swagger.html', extra_context={'schema_url': 'schema'})
