from django import forms

from product.models import Device, Brand, Product, Category


class AddDeviceForm(forms.Form):
    hostname = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Hostname...',
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        )
    )

    categories = Category.objects.all()
    CATG_CHOICES = [
        (category.name.lower(), category.name.upper()) for category in categories
    ]
    category = forms.CharField(
        label='',
        widget=forms.Select(
            choices=CATG_CHOICES,
            attrs={
                'placeholder': 'Brand...',
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        )
    )

    brands = Brand.objects.all()
    BRAND_CHOICES = [
        (brand.name.lower(), brand.name.upper()) for brand in brands
    ]
    brand = forms.CharField(
        label='',
        widget=forms.Select(
            choices=BRAND_CHOICES,
            attrs={
                'placeholder': 'Brand...',
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        )
    )

    products = Product.objects.all()
    PRODUCT_CHOICES = [
        (product.name.lower(), product.name.upper()) for product in products
    ]
    product = forms.CharField(
        label='',
        widget=forms.Select(
            choices=PRODUCT_CHOICES,
            attrs={
                'placeholder': 'Brand...',
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        )
    )

    class Meta:
        model = Device
        fields = (
            'hostname',
            'brand',
            'product',
        )
