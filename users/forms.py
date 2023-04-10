import re

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, \
    PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.core.validators import validate_email


class LoginForm(forms.Form):
    username = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Identifiant...',
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        )
    )
    password = forms.CharField(
        label='',
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Mot de passe...',
                'class': 'rounded-pill form-control field_white_hover shadow-sm'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = authenticate(username=username.lower(), password=password)
        if re.search('[A-Z]', username):
            raise forms.ValidationError("Le nom d'utilisateur ne contient pas de majuscule...")
        if not user:
            raise forms.ValidationError("Nom d'utilisateur ou mot de passe incorrect...")
        return cleaned_data


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
            'class': 'rounded-pill form-control field_white_hover shadow-sm'
        })
    )
    email = forms.CharField(
        label='',
        max_length=100,
        help_text="L'adresse est utilisée pour confirmer la création de compte",
        widget=forms.TextInput(attrs={
            'placeholder': 'Adresse e-mail...',
            'class': 'rounded-pill form-control field_white_hover shadow-sm'
        })
    )
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
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Mot de passe...',
            'class': 'rounded-pill form-control field_white_hover shadow-sm'
        })
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirmation...',
            'class': 'rounded-pill form-control field_white_hover shadow-sm'
        })
    )

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name',
            'email', 'password1', 'password2'
        )

    def clean_username(self):
        username = self.cleaned_data.get('username').lower()
        if User.objects.filter(username=username.lower()).exists():
            raise forms.ValidationError("Ce nom d'utilisateur existe déjà...")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if User.objects.filter(email=email.lower()).exists():
            raise forms.ValidationError("L'adresse email est déjà utilisée...")
        return email

    def clean_first_name(self):
        return self.cleaned_data.get('first_name').capitalize()

    def clean_last_name(self):
        return self.cleaned_data.get('last_name').capitalize()


class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].help_text = ""
        self.fields['new_password1'].help_text = ""
        self.fields['new_password2'].help_text = ""

    old_password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Ancien mot de passe...',
            'class': 'rounded-pill form-control field_white_hover shadow-sm'
        })
    )

    new_password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Nouveau mot de passe...',
            'class': 'rounded-pill form-control field_white_hover shadow-sm'
        })
    )

    new_password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirmation du mot de passe...',
            'class': 'rounded-pill form-control field_white_hover shadow-sm'
        })
    )

    class Meta:
        model = User
        fields = (
            'old_password','new_password1', 'new_password2'
        )


class ChangeFullnameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].help_text = ""
        self.fields['last_name'].help_text = ""

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

    class Meta:
        model = User
        fields = (
            'first_name','last_name'
        )


class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].help_text = "Saisir l'adresse email associée au compte"

    email = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Adresse e-mail...',
            'class': 'rounded-pill form-control field_white_hover shadow-sm'
        })
    )

    class Meta:
        model = User
        fields = 'email'


class ResetPasswordConfirmForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].help_text = ""
        self.fields['new_password2'].help_text = ""

    new_password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Nouveau mot de passe...',
            'class': 'rounded-pill form-control field_white_hover shadow-sm'
        })
    )

    new_password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirmation du mot de passe...',
            'class': 'rounded-pill form-control field_white_hover shadow-sm'
        })
    )
