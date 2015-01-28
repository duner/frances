from django.shortcuts import render
from django.views.generic import TemplateView, View

import frances.main.models as models;


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context
