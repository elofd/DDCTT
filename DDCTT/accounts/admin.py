"""
Admin for accounts app
"""
from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class AccountsAdmin(admin.ModelAdmin):
    """
    Class AccountsAdmin for model CustomUser
    """
    list_display = 'username', 'email'
