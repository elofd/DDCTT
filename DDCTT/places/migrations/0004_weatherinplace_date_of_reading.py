# Generated by Django 4.2.1 on 2023-06-03 01:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_weatherinplace'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherinplace',
            name='date_of_reading',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]