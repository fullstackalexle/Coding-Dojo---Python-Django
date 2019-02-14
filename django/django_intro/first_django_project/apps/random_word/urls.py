from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^random_word$', views.generate_random_word),
    url(r'^generate_random_word$', views.generate_random_word),
    url(r'^random_word\/reset$', views.reset_counter)
]