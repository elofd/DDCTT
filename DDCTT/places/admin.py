# from django.contrib.gis import admin
# from django.contrib.gis.forms import PointField
from django import forms
from django.contrib import admin
# from leaflet.admin import LeafletGeoAdmin

from .models import Place


class PlaceAdminForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'
    # location = PointField(widget=LeafletGeoAdmin)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    # form = PlaceAdminForm
    pass
