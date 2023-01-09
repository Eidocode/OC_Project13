from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^last_users/', views.show_last_users, name='show_last_users'),
    url(r'^all_users/', views.show_all_users, name='show_all_users'),
    url(r'^user_info/(?P<user_id>[0-9]+)/$', views.show_user_info, name='show_user_info'),

    url(r'^last_devices/', views.show_last_devices, name='show_last_devices'),
    url(r'^all_devices/', views.show_all_devices, name='show_all_devices'),
    url(r'^device_info/(?P<device_id>[0-9]+)/$', views.show_device_info, name='show_device_info'),
    url(r'^add_device/', views.add_device, name='add_new_device'),
]
