from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import (ValidationError, datetime_in_current_week_validator,
                         name_validator)


class Schedule(models.Model):
    name = models.CharField(
        max_length=64,

        verbose_name=_('schedule name'),
        help_text=_('schedule name'),

        validators=[name_validator]
    )

    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='schedules',

        verbose_name=_('user'),
        help_text=_('user for this schedule')
    )

    def __str__(self):
        return f'{self.user}: {self.name}'

    class Meta:
        unique_together = [('user', 'name')]

        verbose_name = _('schedule')
        verbose_name_plural = _('schedules')


class Meet(models.Model):
    name = models.CharField(
        max_length=64,

        verbose_name=_('meet name'),
        help_text=_('meet name'),

        validators=[name_validator]
    )

    url = models.URLField(
        verbose_name=_('url'),
        help_text=_('meet url')
    )

    start_datetime = models.DateTimeField(
        verbose_name=_('start datetime'),
        help_text=_('current week\'s start datetime for this meet in format %s' %
                    settings.DATETIME_INPUT_FORMATS[0]),

        validators=[datetime_in_current_week_validator]
    )

    end_datetime = models.DateTimeField(
        verbose_name=_('end datetime'),
        help_text=_('current week\'s end datetime for this meet in format %s' %
                    settings.DATETIME_INPUT_FORMATS[0]),

        validators=[datetime_in_current_week_validator]
    )

    schedule = models.ForeignKey(
        to=Schedule,
        on_delete=models.CASCADE,
        related_name='meets',

        verbose_name=_('schedule'),
        help_text=_('schedule for this meet')
    )

    def clean(self):
        if self.start_datetime >= self.end_datetime:
            raise ValidationError(
                _('start must be before end.'))

        if hasattr(self, 'schedule') and self.schedule is not None:
            for meet in self.schedule.meets.all():
                if (meet.start_datetime < self.start_datetime < meet.end_datetime) or \
                        (meet.start_datetime < self.end_datetime < meet.end_datetime):
                    raise ValidationError(
                        _('ongoing meet at this start/end datetime.'))

        return super().clean()

    def __str__(self):
        return f'{self.name} on {self.start_datetime.date()} at {self.start_datetime.time()}'

    class Meta:
        ordering = ['start_datetime']
        verbose_name = _('meet')
        verbose_name_plural = _('meets')
