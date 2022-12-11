from django.conf.urls import url
from django.urls import path, include

from .views import signup, account, activate

urlpatterns = [
    url(r'^signup/', signup, name='signup'),
    url(r'^account/', account, name='account'),

    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('', include("django.contrib.auth.urls")),
]
