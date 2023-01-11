from django import forms

from product.models import Device, Brand, Product, Category, Cpu, Inventory


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

    category = forms.ModelChoiceField(
        label='',
        queryset=Category.objects.all(),
        empty_label="Catégorie...",
        widget=forms.Select(
            attrs={
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        )
    )

    brand = forms.ModelChoiceField(
        label='',
        queryset=Brand.objects.all(),
        empty_label="Marque...",
        widget=forms.Select(
            attrs={
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        )
    )

    product = forms.ModelChoiceField(
        label='',
        queryset=Product.objects.all(),
        empty_label="Modèle...",
        widget=forms.Select(
            attrs={
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        )
    )

    cpu = forms.ModelChoiceField(
        label='',
        queryset=Cpu.objects.all(),
        empty_label="CPU...",
        widget=forms.Select(
            attrs={
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        )
    )

    ram = forms.CharField(
        label='',
        max_length=5,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ram(Go)...',
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        )
    )

    storage = forms.CharField(
        label='',
        max_length=6,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Stockage(Go)...',
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        )
    )

    serial = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'N° Série...',
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        )
    )

    addr_mac = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'placeholder': '@MAC...',
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        )
    )

    inv_number = forms.CharField(
        label='',
        max_length=6,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'N° Inventaire...',
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        )
    )

    bc_number = forms.CharField(
        label='',
        max_length=12,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'N° BC...',
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
