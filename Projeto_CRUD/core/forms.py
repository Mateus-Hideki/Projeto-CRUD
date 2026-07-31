from django import forms
from .models import Roupa

class RoupaForm(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = [
            'categoria',
            'modelo',
            'cor',
            'tamanho',
            'quantidade',
            'disponivel'
        ]