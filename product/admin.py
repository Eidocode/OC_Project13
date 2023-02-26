from django.contrib import admin

from .models import DeviceUser, Device, Category, Entity, Status, Assignment


admin.site.site_header = 'OC-Inventory Admin Area'


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def get_serial(self, obj):
        return obj.inventory.serial
    get_serial.short_description = 'Serial'

    def get_brand(self, obj):
        return obj.product.brand.name
    get_brand.short_description = 'Brand'

    search_fields = [
        'inventory__hostname',
        "inventory__serial",
        "inventory__addr_mac",
    ]
    list_display = ('inventory', 'get_serial', 'get_brand')
    list_filter = (
        'product__category__name',
        'product__brand__name',
        'inventory__cpu__cpu_brand__name',
        'inventory__storage',
        'inventory__ram',
    )

    fieldsets = (
        ('Informations', {
            'fields': ('inventory', 'product', 'added_date'),
        }),
        ('Immobilisation', {
            'fields': ('immo', 'device_user'),
        })
    )
    readonly_fields = ("added_date", "product", "inventory", "immo")
    exclude = ()


class ProductInline(admin.TabularInline):
    model = Device
    max_num = 0
    fieldsets = (
        ('Informations', {
            'fields': ('inventory', 'product', 'added_date'),
        }),
        ('Immobilisation', {
            'fields': ('immo', 'device_user'),
        })
    )
    readonly_fields = ("added_date", "product", "inventory", "immo")
    verbose_name = 'Périphérique associé'
    verbose_name_plural = 'Périphériques associés'


@admin.register(DeviceUser)
class DeviceUserAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    search_fields = ["uid", "first_name", "last_name"]
    list_display = ("uid", "first_name", "last_name", "email")
    list_filter = ("status", "assignment")

    fieldsets = (
        ('Informations', {
            'fields': ('uid', 'first_name', 'last_name', 'email'),
        }),
        ('Affectation', {
            'fields': ('status', 'assignment'),
        }),
    )
    inlines = [ProductInline]
    readonly_fields = ("uid", "first_name", "last_name", "email")



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