import os
import re
import requests

from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.template.defaultfilters import slugify
from django.contrib.gis.utils import LayerMapping

from frances.main.models import *

import statestyle
from bs4 import BeautifulSoup

class Command(BaseCommand):
	def handle(self, *args, **options):

		HistoricPlace.objects.all().delete()

		mapping = {
			'name' : 'Name',
			'point' : 'POINT',
			'description': 'Description'
		}

		kml_file = os.path.abspath('frances/main/data/doc.kml')
		lm = LayerMapping(HistoricPlace, kml_file, mapping)
		lm.save(verbose=True)

		def match_property_from_description(place, pattern, state=False):
			if place.description:
				match = pattern.search(place.description)
				if match:
					prop = match.group(0)
					if state:
						prop = statestyle.get(prop).name
					return prop
			return None

		places = HistoricPlace.objects.all()

		for place in places:
			state_pattern = re.compile("(?<=State: </b>)[A-Z]*")
			ref_num_pattern = re.compile("(?<=NPS Reference Number: </b>)[0-9]*")

			place.slug = slugify(place.name)
			place.state = match_property_from_description(place, state_pattern, state=True)
			place.ref_num = match_property_from_description(place, ref_num_pattern)

			try:
				place.save()
			except IntegrityError:
				place.delete()


		WIKIPEDIA_BASE_URL = 'http://en.wikipedia.org'

		def get_state_wikipedia_page(state):
			url = 'http://en.wikipedia.org/wiki/Category:National_Register_of_Historic_Places_lists_by_state'
			html = requests.get(url)
			soup = BeautifulSoup(html.content, 'html.parser')
			divs = soup.find_all('div', class_='mw-content-ltr')
			links = divs[0].findAll('a', text=re.compile(state))
			return WIKIPEDIA_BASE_URL + links[0].attrs['href']

		def get_table_from_county_page(county_url):
			html = requests.get(county_url)
			soup = BeautifulSoup(html.content, 'html.parser')
			headers = soup.find_all('h2')
			for head in headers:
				spans = head.find_all('span', text=re.compile('listing'), class_='mw-headline')
				if len(spans) > 0:
					table = head.find_next_sibling('table')
					if table:
						return table
				else:
					return None

		def get_county_tables(state_url):
			links = []
			county_tables = []
			html = requests.get(state_url)
			soup = BeautifulSoup(html.content, 'html.parser')

			headers = soup.find_all('h2')
			for head in headers:
				spans = head.find_all('span', text=re.compile('Numbers'), class_='mw-headline')
				if len(spans) > 0:
					table = head.find_next_sibling()
					rows = table.find_all('tr')
					for row in rows[1:-2]:
						cell = row.find_all('td')[1]
						link = cell.find('a')
						if link:
							links.append(link.attrs['href'])

			for link in links:
				if 'wiki' in link:
					table = get_table_from_county_page(WIKIPEDIA_BASE_URL + link)
				else:
					span_id = link.split('#')[1]
					h2 = soup.find('span', id=span_id).find_parent('h2')
					table = h2.find_next_sibling()
				county_tables.append(table)
			return county_tables

		def get_places_from_table(table):
			places = []
			for row in table.find_all('tr')[1:]:
				place = {}
				data = row.find_all('td')
				
				#Get Ref Num
				span = data[2].find('center').find('span', class_="refnum")
				ref_num = span.find_all(['a','small'], text=re.compile('[0-9]*'))[0].string
				ref_num = re.sub(r'\W+', '', ref_num)
				place['ref_num'] = ref_num

				#Get URL
				place['url'] = data[0].find('a').attrs['href']

				places.append(place)
			return places

		def save_wiki_place(place):
			try:
				p = HistoricPlace.objects.get(ref_num=place['ref_num'])
				p.wikipedia_url = WIKIPEDIA_BASE_URL + place['url']
				p.save()
				print p.name
			except ObjectDoesNotExist:
				print("Either the entry or blog doesn't exist.")


		def scrape_wikipedia():
			for state in HistoricPlace.objects.values('state').distinct():
				state = state.get('state')
				if state:
					state_url = get_state_wikipedia_page(state)
					county_tables = get_county_tables(state_url)
					for table in county_tables:
						if table:
							places = get_places_from_table(table)
							for place in places:
								save_wiki_place(place)
						else:
							print table

		scrape_wikipedia()

			