from django.contrib.gis.db import models
import re

class HistoricPlace(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    slug = models.SlugField(max_length=250, blank=True, null=True, unique=True)
    ref_num = models.CharField(max_length=100, blank=True, null=True, unique=True)
    point = models.PointField(srid=900913)
    objects = models.GeoManager()

    state = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    county = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_listed = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    wikipedia_url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name