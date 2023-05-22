from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """
    Кастомный пользователь "чтоб было"
    Сделал уникальным email, потом можно расширить
    """
    email = models.EmailField(_('email address'), unique=True)
