from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^show_user/', views.show_product_user, name='show_product_user'),
]
