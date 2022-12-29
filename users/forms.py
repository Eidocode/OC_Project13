from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        label='',
        max_length=50,
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Identifiant...',
                'class': 'rounded-pill form-control shadow-sm'
            }
        )
    )
    password = forms.CharField(
        label='',
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Mot de passe...',
                'class': 'rounded-pill form-control shadow-sm'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )


class SignupForm(UserCreationForm):
    """
    Used when registering a new user
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text = ""

    username = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Identifiant...',
            'class': 'rounded-pill form-control'
        })
    )
    email = forms.CharField(
        label='',
        max_length=100,
        help_text="L'adresse est utilisée pour confirmer la création du compte",
        widget=forms.TextInput(attrs={
            'placeholder': 'Adresse e-mail...',
            'class': 'rounded-pill form-control'
        })
    )
    first_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Prénom...',
            'class': 'rounded-pill form-control'
        })
    )
    last_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nom...',
            'class': 'rounded-pill form-control'
        })
    )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Mot de passe...',
            'class': 'rounded-pill form-control'
        })
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirmation...',
            'class': 'rounded-pill form-control'
        })
    )

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name',
            'email', 'password1', 'password2'
        )
