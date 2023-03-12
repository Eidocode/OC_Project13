from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<device_type>[\w ]+)/$', views.dashboard, name='dashboard_filter'),
    url(r'^$', views.dashboard, name='dashboard'),

    # url(r'^devices/(?P<device_type>\w+)/$', views.device_list, name='device_list'),
    # url(r'^devices/$', views.device_list, name='device_list_all'),
]
