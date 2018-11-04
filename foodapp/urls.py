from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.restaurant_list, name='restaurant_list'),
    url(r'^(?P<pk>\w+)/$', views.restaurant_detail, name='restaurant_detail'),
    url(r'^(?P<pk>\w+)/add_review/$', views.add_review, name='add_review'),
]
