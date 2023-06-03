"""
Views for news app
"""
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import News
from .serializers import NewsSerializer


class NewsListCreateView(ListCreateAPIView):
    """
    class NewsListCreateViews for News model
    """
    queryset = News.objects.select_related('author').all()
    serializer_class = NewsSerializer


class NewsUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    class NewsUpdateDeleteView for News model
    """
    queryset = News.objects.select_related('author').all()
    serializer_class = NewsSerializer
