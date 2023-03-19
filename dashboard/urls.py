from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^advanced_search/$', views.advanced_search, name='advanced_search'),
    url(r'^show_device_table/$', views.show_device_table, name='show_device_table'),
    url(r'^(?P<device_type>[\w ]+)/$', views.dashboard, name='dashboard_filter'),
    url(r'^$', views.dashboard, name='dashboard'),
]
