from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^contact_us/', views.contact_us, name='contact_us'),
    url(r'^mentions/', views.mentions, name='mentions'),
]
