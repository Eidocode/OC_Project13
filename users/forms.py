from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    """
    Used when registering a new user
    """
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(max_length=200, help_text='Enter a valid address')

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name',
            'email', 'password1', 'password2'
        ]
