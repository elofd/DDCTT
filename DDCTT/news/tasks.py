from datetime import datetime

from constance import config
from django.core.mail import send_mail
from DDCTT.DDCTT.celery import app

from .models import News


@app.task
def send_news_email():
    today = datetime.now().date()
    news = News.objects.filter(created_date__date=today)
    if news:
        recipients = config.EMAIL_RECIPIENTS
        subject = config.EMAIL_SUBJECT
        message = config.EMAIL_TEXT + '\n\n'
        for i_news in news:
            message += f'{i_news.title}\n{i_news.description}\n\n'
        send_mail(subject, message, 'from@example.com', recipients)