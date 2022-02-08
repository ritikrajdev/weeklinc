import django_filters
from django_filters import rest_framework as filters

from .models import Meet, Schedule


# Filters
class ModelChoiceFilter(django_filters.ModelChoiceFilter):
    def get_queryset(self, request):
        if request.user.is_authenticated:
            return request.user.schedules.all()
        return Schedule.objects.none()


# FilterSets
class MeetFilterSet(filters.FilterSet):
    schedule = ModelChoiceFilter()

    class Meta:
        model = Meet
        fields = ['name', 'start_datetime', 'end_datetime', 'schedule']
