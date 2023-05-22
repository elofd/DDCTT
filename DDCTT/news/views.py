from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import News
from .serializers import NewsSerializer


class NewsListCreateView(ListCreateAPIView):
    """
    Просматривае создаём экземпляры модели News
    """
    queryset = News.objects.select_related('author').all()
    serializer_class = NewsSerializer


class NewsUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    Изменяем удаляем экземпляры модели News
    """
    queryset = News.objects.select_related('author').all()
    serializer_class = NewsSerializer