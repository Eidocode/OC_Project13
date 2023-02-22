from django.contrib import admin

import django.apps

from .models import Inventory, DeviceUser, Device, Product, Brand, Category, \
    Entity, Location, Status, Assignment, CpuBrand, Cpu


class InventoryAdminArea(admin.AdminSite):
    site_header = 'OC-Inventory Admin Area'


admin_inventory_site = InventoryAdminArea(name='inventory_admin')

admin_inventory_site.register(Inventory)

# class InventoryInline(admin.TabularInline):
#     model = Device
#     fieldsets = [
#         (None, {'fields': ['device_user']}),
#     ]
#     extra = 0
#     verbose_name = 'Utilisateur affecté'
#     verbose_name_plural = 'Utilisateurs affectés'
#
#
# @admin.register(Inventory)
# class InventoryAdmin(admin.ModelAdmin):
#     inlines = [InventoryInline]
#     exclude = ("hostname", "serial", "cpu", "ram", "addr_mac", "storage")
#     readonly_fields = ("hostname", "serial", "cpu", "ram", "addr_mac", "storage")


# @admin.register(Device, Product)
# class DeviceAdmin(admin.ModelAdmin):
#     exclude = ("added_date",)
#     readonly_fields = ("added_date",)

#
# @admin.register(Brand)
# class DeviceAdmin(admin.ModelAdmin):
#     def get_model_perms(self, request):
#         """
#         Return empty perms dict thus hiding the model from admin index.
#         """
#         return {}
#
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     def get_model_perms(self, request):
#         """
#         Return empty perms dict thus hiding the model from admin index.
#         """
#         return {}
#
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     fields = ('category', 'brand', 'name')
#
#
# @admin.register(Status)
# class StatusAdmin(admin.ModelAdmin):
#     def get_model_perms(self, request):
#         """
#         Return empty perms dict thus hiding the model from admin index.
#         """
#         return {}
#
#
# @admin.register(Assignment)
# class AssignmentAdmin(admin.ModelAdmin):
#     def get_model_perms(self, request):
#         """
#         Return empty perms dict thus hiding the model from admin index.
#         """
#         return {}
#
#
# @admin.register(DeviceUser)
# class DeviceUserAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(CpuBrand)
# class CpuBrandAdmin(admin.ModelAdmin):
#     def get_model_perms(self, request):
#         """
#         Return empty perms dict thus hiding the model from admin index.
#         """
#         return {}
#
#
# @admin.register(Cpu)
# class CpuAdmin(admin.ModelAdmin):
#     def get_model_perms(self, request):
#         """
#         Return empty perms dict thus hiding the model from admin index.
#         """
#         return {}
#
#
# @admin.register(Inventory)
# class InventoryAdmin(admin.ModelAdmin):
#     pass
