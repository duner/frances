from django.contrib.gis.db import models
import re

class HistoricPlace(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    point = models.PointField(srid=900913)
    description = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=150, blank=True, null=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name
