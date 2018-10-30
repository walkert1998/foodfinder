from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.restaurant_list, name='restaurant_list'),
    url(r'^(?P<pk>\d+)/$', views.restaurant_detail, name='restaurant_detail'),
]
