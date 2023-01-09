from django import forms

from product.models import Device


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

    brand = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Brand...',
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        )
    )

    FRUIT_CHOICES = [
        ('test1', 'Test1'),
        ('test2', 'Test2'),
        ('test3', 'Test3'),
        ('test4', 'Test4'),
    ]

    product = forms.CharField(
        label='',
        widget=forms.Select(
            choices=FRUIT_CHOICES,
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
