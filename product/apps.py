from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class InventoryAdminConfig(AdminConfig):
    default_site = 'product.admin.InventoryAdminArea'

class ProductConfig(AppConfig):
    name = 'product'
