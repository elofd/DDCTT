"""
Admin for news app
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import News


@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    """
    class NewsAdmin for News model
    """
    list_display = 'title', 'created_date', 'author'
    summernote_fields = 'description',
    fields = 'title', 'main_image', 'preview', 'description', 'author'
    readonly_fields = 'preview',
