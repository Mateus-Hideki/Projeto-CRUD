from django import forms
from .models import Roupa, Categoria, Modelo

class RoupaForm(forms.ModelForm):
    categoria_text = forms.CharField(required=False, max_length=150, label='Categoria')
    modelo_text = forms.CharField(required=False, max_length=150, label='Modelo')

    class Meta:
        model = Roupa
        fields = ['cor', 'tamanho', 'quantidade']

    def save(self, commit=True):
        instance = super().save(commit=False)

        categoria_nome = (self.cleaned_data.get('categoria_text') or '').strip()
        modelo_nome = (self.cleaned_data.get('modelo_text') or '').strip()

        if categoria_nome:
            categoria_obj, _ = Categoria.objects.get_or_create(categoria=categoria_nome)
            instance.categoria = categoria_obj

        if modelo_nome:
            categoria_obj = instance.categoria
            modelo_obj, _ = Modelo.objects.get_or_create(modelo=modelo_nome, categoria=categoria_obj)
            instance.modelo = modelo_obj

        if commit:
            instance.save()

        return instance

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria']

class ModeloForm(forms.ModelForm):
    categoria_text = forms.CharField(required=False, max_length=150, label='Categoria')

    class Meta:
        model = Modelo
        fields = ['modelo']

    def save(self, commit=True):
        instance = super().save(commit=False)

        categoria_nome = (self.cleaned_data.get('categoria_text') or '').strip()
        if categoria_nome:
            categoria_obj, _ = Categoria.objects.get_or_create(categoria=categoria_nome)
            instance.categoria = categoria_obj

        if commit:
            instance.save()

        return instance
