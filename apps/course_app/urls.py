from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^removed/(?P<id>\d+)$', views.remove),
    url(r'^removed/(?P<id>\d+)/destroy$', views.destroy),

]
