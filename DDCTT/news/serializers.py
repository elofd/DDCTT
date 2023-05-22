from rest_framework.serializers import ModelSerializer

from .models import News


class NewsSerializer(ModelSerializer):
    """
    Сериалайзер для модели News
    """
    class Meta:
        model = News
        fields = '__all__'