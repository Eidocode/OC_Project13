"""
Forms used for user management
"""

import re

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, \
    PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """
    User login form
    """
    username = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Identifiant...',
                'class': """rounded-pill form-control field_white_hover
                            shadow-sm"""
            }
        )
    )
    password = forms.CharField(
        label='',
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Mot de passe...',
                'class': """rounded-pill form-control field_white_hover
                            shadow-sm"""
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
        """
        Validate the form data

        :return: username and password cleaned data
        """
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Try to authenticate the user
        user = authenticate(username=username.lower(), password=password)
        # If an uppercase letter is found, raise an error
        if re.search('[A-Z]', username):
            raise forms.ValidationError(
                "Le nom d'utilisateur ne contient pas de majuscule...")
        # if user is not found, raise an error
        if not user:
            raise forms.ValidationError(
                "Nom d'utilisateur ou mot de passe incorrect...")
        return cleaned_data


class SignupForm(UserCreationForm):
    """
    Signup form
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
        help_text="Adresse utilisée pour confirmer la création de compte",
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
        """
        Validate the username

        :return: username cleaned data
        """
        # Gets username cleaned data and lower it
        username = self.cleaned_data.get('username').lower()
        # Checks if username already exists
        if User.objects.filter(username=username.lower()).exists():
            raise forms.ValidationError("Ce nom d'utilisateur existe déjà...")
        return username

    def clean_email(self):
        """
        Validate the email

        :return: email cleaned data
        """
        # Gets email cleaned data and lower it
        email = self.cleaned_data.get('email').lower()
        # Checks if email already exists
        if User.objects.filter(email=email.lower()).exists():
            raise forms.ValidationError("L'adresse email est déjà utilisée...")
        return email

    def clean_first_name(self):
        """
        Validate the first name

        :return: first name capitalized cleaned data
        """
        return self.cleaned_data.get('first_name').capitalize()

    def clean_last_name(self):
        """
        Validate the last name

        :return: last name capitalized cleaned data
        """
        return self.cleaned_data.get('last_name').capitalize()


class ChangePasswordForm(PasswordChangeForm):
    """
    Change password form
    """
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
            'old_password', 'new_password1', 'new_password2'
        )


class ChangeFullnameForm(forms.ModelForm):
    """
    Change fullname form
    """
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
            'first_name', 'last_name'
        )


class ResetPasswordForm(PasswordResetForm):
    """
    Reset password form
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].help_text = "Saisir l'email associée au compte"

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
    """
    Reset password confirm form
    """
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
