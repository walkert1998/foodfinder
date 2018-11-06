from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.restaurant_list, name='restaurant_list'),
    url(r'^restaurant/(?P<slug>[\w-]+)/$', views.restaurant_detail, name='restaurant_detail'),
    url(r'^restaurant/(?P<slug>[\w-]+)/add_review/$', views.add_review, name='add_review'),
    url(r'^restaurants/(?P<slug>[\w-]+)/$', views.restaurant_types, name='restaurant_types'),
]
