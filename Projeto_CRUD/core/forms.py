from django import forms
from .models import Roupa, Categoria, Modelo

class RoupaForm(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = [
            'categoria',
            'modelo',
            'cor',
            'tamanho',
            'quantidade'
        ]

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'categoria'
        ]

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = [
            'categoria',
            'modelo'
        ]
