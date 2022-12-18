from django.conf.urls import url
from django.urls import path, include

from .views import signup, account, activate, change_password

urlpatterns = [
    url(r'^signup/', signup, name='signup'),
    url(r'^account/', account, name='account'),
    url(r'^changepwd/$', change_password, name='change_password'),

    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('', include("django.contrib.auth.urls")),
]
