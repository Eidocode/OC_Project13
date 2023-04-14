from django.contrib import admin

from .models import DeviceUser, Device, Category

# Set the admin area title
admin.site.site_header = 'OC-Inventory Admin Area'


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        """Disable adding new devices in the admin area"""
        return False

    # Define the serial number field
    def get_serial(self, obj):
        return obj.inventory.serial
    get_serial.short_description = 'Serial'

    # Define the brand field
    def get_brand(self, obj):
        return obj.product.brand.name
    get_brand.short_description = 'Brand'

    # Enable searching by this filters
    search_fields = [
        'inventory__hostname',
        "inventory__serial",
        "inventory__addr_mac",
    ]
    # Set the list of fields to be displayed
    list_display = ('inventory', 'get_serial', 'get_brand')
    # Set the list of fields to be displayed in the filters
    list_filter = (
        'product__category__name',
        'product__brand__name',
        'inventory__cpu__cpu_brand__name',
        'inventory__storage',
        'inventory__ram',
    )

    # Set the fieldsets to be displayed
    fieldsets = (
        ('Informations', {
            'fields': ('inventory', 'product', 'added_date'),
        }),
        ('Immobilisation', {
            'fields': ('immo', 'device_user'),
        })
    )
    # Set the readonly fields
    readonly_fields = ("added_date", "product", "inventory", "immo")
    exclude = ()


class ProductInline(admin.TabularInline):
    """
    Inline admin for the Product model
    """
    model = Device
    max_num = 0
    extra = 1
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
    can_delete = False  # Prevents deletion of objects linked to foreign keys


@admin.register(DeviceUser)
class DeviceUserAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        """Disable adding new devices in the admin area"""
        return False

    # Enable searching by this fields
    search_fields = ["uid", "first_name", "last_name"]
    # Set the fields to be displayed
    list_display = ("uid", "first_name", "last_name", "email")
    # Set the fields to use as filters
    list_filter = ("status", "assignment")

    # Define the fieldsets to be displayed
    fieldsets = (
        ('Informations', {
            'fields': ('uid', 'first_name', 'last_name', 'email'),
        }),
        ('Affectation', {
            'fields': ('status', 'assignment'),
        }),
    )
    # Add the inline for the device model
    inlines = [ProductInline]
    # Set the readonly fields
    readonly_fields = ("uid", "first_name", "last_name", "email")

    @admin.register(Category)
    class CategoryAdmin(admin.ModelAdmin):
        pass
