# Generated by Django 4.2 on 2023-05-18 16:33

from django.db import migrations
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=django_summernote.fields.SummernoteTextField(),
        ),
    ]