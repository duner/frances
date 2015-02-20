from django.conf.urls import patterns, include, url
from django.contrib import admin

from main import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'frances.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.HomeView.as_view(), name='home'),

 	url(r'^places/list', views.HistoricPlaceListView.as_view(), name='place-list'),

 	url(r'^place/(?P<slug>[\w-]+)/*$', views.HistoricPlaceDetailView.as_view(), name='place-detail')

)
