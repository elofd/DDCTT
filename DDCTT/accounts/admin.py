from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class AccountsAdmin(admin.ModelAdmin):
    """
    Админка для модели CustomUser
    """
    list_display = 'username', 'email'