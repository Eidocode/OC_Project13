from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, \
    PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(
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
            'class': 'rounded-pill form-control shadow-sm'
        })
    )
    email = forms.CharField(
        label='',
        max_length=100,
        help_text="L'adresse est utilisée pour confirmer la création du compte",
        widget=forms.TextInput(attrs={
            'placeholder': 'Adresse e-mail...',
            'class': 'rounded-pill form-control shadow-sm'
        })
    )
    first_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Prénom...',
            'class': 'rounded-pill form-control shadow-sm'
        })
    )
    last_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nom...',
            'class': 'rounded-pill form-control shadow-sm'
        })
    )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Mot de passe...',
            'class': 'rounded-pill form-control shadow-sm'
        })
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirmation...',
            'class': 'rounded-pill form-control shadow-sm'
        })
    )

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name',
            'email', 'password1', 'password2'
        )


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
            'class': 'rounded-pill form-control shadow-sm'
        })
    )

    new_password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Nouveau mot de passe...',
            'class': 'rounded-pill form-control shadow-sm'
        })
    )

    new_password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirmation du mot de passe...',
            'class': 'rounded-pill form-control shadow-sm'
        })
    )

    class Meta:
        model = User
        fields = (
            'old_password','new_password1', 'new_password2'
        )


class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].help_text = "Saisir l'email du compte à réinitialiser"

    email = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Adresse e-mail...',
            'class': 'rounded-pill form-control shadow-sm'
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
            'class': 'rounded-pill form-control shadow-sm'
        })
    )

    new_password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirmation du mot de passe...',
            'class': 'rounded-pill form-control shadow-sm'
        })
    )
