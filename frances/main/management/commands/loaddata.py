import os
from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.utils import LayerMapping
from frances.main.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):

		mapping = {
		    'name' : 'Name',
		    'point' : 'POINT',
		    'description': 'Description'
		}

		kml_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/doc.kml'))

		lm = LayerMapping(HistoricPlace, kml_file, mapping)
		lm.save(verbose=True)