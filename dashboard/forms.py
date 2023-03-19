from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'id_search',
                'class': 'form-control border-left-0 border-right-0 form-control-lg bg-light shadow',
                'placeholder': 'Saisir la recherche...'
            }
        ),
    )

    FILTER_CHOICES = [
        ('category', 'Type'),
        ('brand', 'Marque'),
        ('entity', 'Entité'),
        ('serial', 'N°série'),
        ('hostname', 'Périphérique'),
        ('inventory', 'N°Inventaire'),
        ('user', 'Utilisateur'),
    ]
    search_filter = forms.ChoiceField(
        choices=FILTER_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'btn btn-dark border-right-0 shadow',
            }
        ),
        required=False
    )
