from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows/new$', views.new_show),
    url(r'^shows/create$', views.create_show),
    url(r'^shows/(?P<id>\d+)$', views.show_show),
    url(r'^shows/(?P<id>\d+)/edit$', views.edit_show),
    url(r'^shows/(?P<id>\d+)/update$', views.update_show),
    url(r'^shows/(?P<id>\d+)/delete$', views.delete_show)
]