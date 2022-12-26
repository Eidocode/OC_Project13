from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    """
    Used when registering a new user
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = """
            <ul>
            <li>Minimum 8 caractères</li>
            <li>Pas entièrement numérique</li>
            </ul>
        """
        self.fields['password2'].help_text = """
            Saisir le même mot de passe que précédemment 
        """
        self.helper.form_class = 'blueForms'

    username = UsernameField(label='Identifiant', max_length=50)
    first_name = forms.CharField(label='Prénom', max_length=50)
    last_name = forms.CharField(label='Nom', max_length=50)
    email = forms.EmailField(
        label='E-mail',
        max_length=100,
        help_text="L'adresse est utilisée pour confirmer la création du compte"
    )


    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name',
            'email', 'password1', 'password2'
        )
