# from django.contrib.gis.db import models
from django.db import models
from django.utils.translation import gettext_lazy as _



class Place(models.Model):
    """
    Модель для примечательных мест
    """
    name = models.CharField(_('name'), max_length=250)
    # point = models.PointField()
    raiting = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

