"""
Serializers for news app
"""
from rest_framework.serializers import ModelSerializer

from .models import News


class NewsSerializer(ModelSerializer):
    """
    class NewsSerializers for News model
    """
    class Meta:
        model = News
        fields = '__all__'
