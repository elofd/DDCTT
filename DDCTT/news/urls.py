from django.urls import path

from .views import NewsListCreateView, NewsUpdateDeleteView


app_name = 'news'

urlpatterns = [
    path('', NewsListCreateView.as_view(), name='news_list_create'),
    path('<int:pk>/', NewsUpdateDeleteView.as_view(), name='news_update_delete'),
]