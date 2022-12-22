from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    url(r'^signup/', views.signup, name='signup'),
    url(r'^account/', views.account, name='account'),
    url(r'^change_pwd/$', views.change_password, name='change_password'),
    # url(r'^reset_pwd/$', views.reset_password, name='reset_password'),

    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    # path('reset/<uidb64>/<token>', views.reset_password_confirm, name='reset_password_confirm'),
    path('', include("django.contrib.auth.urls")),
]
