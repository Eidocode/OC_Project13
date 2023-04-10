from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'id_search',
                'class': 'form-control border-left-0 border-right-0 form-control-lg bg-light',
                'placeholder': 'Saisir la recherche...'
            }
        ),
    )

    FILTER_CHOICES = [
        ('device', 'Périphérique'),
        ('entity', 'Entité'),
        ('user', 'Utilisateur'),
    ]
    search_filter = forms.ChoiceField(
        choices=FILTER_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'btn btn-dark border-right-0',
            }
        ),
        required=False
    )

    device_without_user = forms.BooleanField(
        required=False,
    )
