from datetime import datetime

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

name_validator = RegexValidator(
    '^[a-zA-Z0-9-_]*$', _('only english characters, numbers, - and _ are allowed allowed.'))


def datetime_in_current_week_validator(value: datetime):
    now = timezone.now()
    if abs((value - now).days) >= 7:
        raise ValidationError(_('datetime must be in this week only.'))
