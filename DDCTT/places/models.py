"""
Models for places app
"""
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class Place(models.Model):
    """
    class Place model
    """
    name = models.CharField(_('name'), max_length=250)
    point = models.PointField()
    raiting = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(25)])

    def __str__(self):
        return self.name


class WeatherInPlace(models.Model):
    """
    class WeatherInPlace model
    """
    temp = models.IntegerField(_('temperature (C)'), default=0)
    humidity = models.IntegerField(_('humidity (%)'), default=0)
    pressure = models.IntegerField(_('pressure (mmhg)'), default=0)
    wind_deg = models.IntegerField(_('direction (°)'), default=0)
    wind_speed = models.IntegerField(_('speed (m/s)'), default=0)
    date_of_reading = models.DateTimeField(auto_now_add=True)
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)

