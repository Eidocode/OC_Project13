from django import forms

from product.models import Inventory, Cpu, Location, Immo, Product, OperatingSystem


class ProductForm(forms.Form):
    name = forms.ModelChoiceField(
        label='',
        queryset=Product.objects.all(),
        empty_label="Product...",
        widget=forms.Select(
            attrs={
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        ),
    )


class InventoryForm(forms.ModelForm):
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
    operating_system = forms.ModelChoiceField(
        label='',
        queryset=OperatingSystem.objects.all(),
        empty_label="Système d'exploitation...",
        widget=forms.Select(
            attrs={
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        )
    )

    class Meta:
        model = Inventory
        fields = (
            'hostname',
            'serial',
            'cpu',
            'ram',
            'addr_mac',
            'storage',
            'operating_system',
        )

    def clean_serial(self):
        serial = self.cleaned_data.get('serial').upper()
        if Inventory.objects.filter(serial=serial.upper()).exists():
            raise forms.ValidationError("Ce numéro de série existe déjà...")
        return self.cleaned_data.get('serial')


class ImmoForm(forms.ModelForm):
    bc_number = forms.CharField(
        label='',
        max_length=12,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'N°BC...',
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        )
    )
    inventory_number = forms.CharField(
        label='',
        max_length=12,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'N°Inventaire...',
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        )
    )

    class Meta:
        model = Immo
        fields = (
            'bc_number',
            'inventory_number',
        )

    def clean_inventory_number(self):
        inventory_number = self.cleaned_data.get('inventory_number')

        if not inventory_number.isdigit():
            raise forms.ValidationError("Le numéro d'inventaire ne doit contenir que des chiffres...")

        if Immo.objects.filter(inventory_number=inventory_number).exists():
            raise forms.ValidationError("Ce numéro d'inventaire existe déjà...")
        return inventory_number


class LocationForm(forms.Form):
    loc_name = forms.ModelChoiceField(
        label='',
        queryset=Location.objects.all(),
        empty_label="Localisation...",
        widget=forms.Select(
            attrs={
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        ),
    )
