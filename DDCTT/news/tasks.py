"""
Celery tasks for news app
"""
from datetime import datetime
import os

from django.core.mail import send_mail
from constance import config

from DDCTT.celery import app
from .models import News


@app.task
def send_news_email_with_constance():
    """
    Send emails with new news with dynamic settings
    """
    today = datetime.now().date()
    news = News.objects.filter(created_date__date=today)
    if news and config.EMAIL_RECIPIENTS:
        subject = f'{config.EMAIL_SUBJECT} for {today}'
        message = config.EMAIL_BODY
        for i_news in news:
            message += f'{i_news.title}\n{i_news.description}\n\n'
        send_mail(
            subject,
            message,
            os.environ.get('MAIL_RU_NAME'),
            config.EMAIL_RECIPIENTS.split(', '),
            fail_silently=False,
        )
