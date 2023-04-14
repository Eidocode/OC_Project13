"""
Form used in the contact us section
"""

from django import forms


class ContactUsForm(forms.Form):
    """
    Contact us form fields
    """
    first_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Prénom...',
            'class': 'rounded-pill form-control field_white_hover shadow-sm'
        })
    )
    last_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nom...',
            'class': 'rounded-pill form-control field_white_hover shadow-sm'
        })
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Adresse e-mail...',
            'class': 'rounded-pill form-control field_white_hover shadow-sm'
        })
    )
    subject = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Objet...',
            'class': 'rounded-pill form-control field_white_hover shadow-sm'
        }),
    )
    message = forms.CharField(
        label='',
        max_length=500,
        widget=forms.Textarea(attrs={
            'placeholder': 'Saisissez votre message...',
            'class': 'rounded-lg form-control field_white_hover shadow-sm'
        }),
        help_text='Message limité à 500 caractères...',
    )
