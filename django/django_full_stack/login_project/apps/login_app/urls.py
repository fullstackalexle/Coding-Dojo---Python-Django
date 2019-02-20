from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/create$', views.create_user),
    url(r'^users/session/create$', views.create_session),
    url(r'^users/logout$', views.destroy_session)
]