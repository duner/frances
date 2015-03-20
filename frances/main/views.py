from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

import frances.main.models as models
import statestyle

class HomeView(TemplateView):
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #     places = models.HistoricPlace.objects.filter
    #     context["places"] = places
    #     return context
    # ALEX, TOOK THESE OUT SO I COULD MAKE INDEX.HTML A HOME PAGE (WITH NO DATA ON IT)


class HistoricPlaceListView(ListView):
	model = models.HistoricPlace
	template_name = 'list.html'
	paginate_by = 25
	context_object_name = 'historic_places'

	def get_queryset(self):
		state = self.request.GET.get('state', None)
		# state = statestyle.get(state).name
		if state: 
			return models.HistoricPlace.objects.filter(state=state)
		return models.HistoricPlace.objects.all()

class HistoricPlaceDetailView(DetailView):
	model = models.HistoricPlace
	template_name = 'details.html'
	context_object_name = 'place'
