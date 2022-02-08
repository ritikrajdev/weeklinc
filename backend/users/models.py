from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(
        verbose_name=_('email'),
        help_text=_('email address'),
        blank=False,
        unique=True
    )

    first_name = None
    last_name = None
    last_login = None
    date_joined = None
