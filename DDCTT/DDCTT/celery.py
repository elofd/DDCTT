"""
Celery settings
"""
import os

from celery import Celery
from celery.schedules import crontab
from constance import config


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DDCTT.settings')

app = Celery('DDCTT')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    f'send-news-every-{config.EMAIL_TIME}-minutes': {
        'task': 'news.tasks.send_news_email_with_constance',
        'schedule': crontab(minute=f'*/{config.EMAIL_TIME}'),
    },
    f'get-places-weather-every-{config.WEATHER_TIME}-minutes': {
        'task': 'places.tasks.get_places_weather',
        'schedule': crontab(minute=f'*/{config.WEATHER_TIME}'),
    },

}
