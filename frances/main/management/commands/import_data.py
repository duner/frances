import os
import re
from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.utils import LayerMapping
from frances.main.models import *
import statestyle


class Command(BaseCommand):

    def handle(self, *args, **options):

		mapping = {
		    'name' : 'Name',
		    'point' : 'POINT',
		    'description': 'Description'
		}

		kml_file = os.path.abspath('frances/main/data/doc.kml')

		lm = LayerMapping(HistoricPlace, kml_file, mapping)
		lm.save(verbose=True)

		def get_state_from_description(place):
			if place.description:
				pattern = re.compile("(?<=State: </b>)[A-Z]*")
				match = pattern.search(place.description)
				if match:
					state = match.group
					state = statestyle.get(state(0)).name
					return state
			else:
				return None


		places = HistoricPlace.objects.all()

		for place in places:
			place.state = get_state_from_description(place)
			place.save()


			