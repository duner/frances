import os
from django.contrib.gis.utils import LayerMapping
from frances.main.models import HistoricPlace

mapping = {
    'name' : 'Name',
    'point' : 'POINT',
    'description': 'Description'
}

kml_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/doc.kml'))

print kml_file

lm = LayerMapping(HistoricPlace, kml_file, mapping)
lm.save(verbose=True)
