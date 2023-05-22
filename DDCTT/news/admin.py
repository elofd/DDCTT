from django.contrib import admin
from django_summernote.widgets import SummernoteWidget
from django_summernote.admin import SummernoteModelAdmin

from .models import News


@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    """
    Админка для модели News
    """
    list_display = 'title', 'created_date', 'author'
    summernote_fields = 'description'
