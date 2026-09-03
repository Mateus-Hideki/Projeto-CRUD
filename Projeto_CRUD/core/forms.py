from django import forms
from .models import Roupa, Categoria, Modelo


class AlterarEstoqueForm(forms.Form):
    operacao = forms.ChoiceField(
        choices=[('adicionar', 'Adicionar unidades'), ('subtrair', 'Subtrair unidades')],
        label='Operação',
    )
    quantidade = forms.IntegerField(min_value=1, label='Quantidade')

    def __init__(self, *args, roupa=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.roupa = roupa

    def clean(self):
        cleaned_data = super().clean()
        if (
            cleaned_data.get('operacao') == 'subtrair'
            and self.roupa
            and cleaned_data.get('quantidade', 0) > self.roupa.quantidade
        ):
            self.add_error('quantidade', 'A quantidade não pode deixar o estoque negativo.')
        return cleaned_data

class RoupaForm(forms.ModelForm):
    categoria_text = forms.CharField(required=False, max_length=150, label='Categoria')
    modelo_text = forms.CharField(required=False, max_length=150, label='Modelo')

    class Meta:
        model = Roupa
        fields = ['cor', 'tamanho', 'quantidade']

    def clean(self):
        cleaned_data = super().clean()
        categoria_nome = (cleaned_data.get('categoria_text') or '').strip()
        modelo_nome = (cleaned_data.get('modelo_text') or '').strip()
        cor = (cleaned_data.get('cor') or '').strip()
        tamanho = (cleaned_data.get('tamanho') or '').strip()

        if modelo_nome and cor and tamanho:
            categoria_obj = None
            if categoria_nome:
                categoria_obj = Categoria.objects.filter(categoria__iexact=categoria_nome).first()
            modelo_obj = Modelo.objects.filter(modelo__iexact=modelo_nome, categoria=categoria_obj).first()
            if modelo_obj and Roupa.objects.filter(
                modelo=modelo_obj,
                cor__iexact=cor,
                tamanho__iexact=tamanho,
            ).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError(
                    'Este produto já existe no estoque. Use "Adicionar estoque" para aumentar a quantidade.'
                )

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        categoria_nome = (self.cleaned_data.get('categoria_text') or '').strip()
        modelo_nome = (self.cleaned_data.get('modelo_text') or '').strip()

        if categoria_nome:
            categoria_obj = Categoria.objects.filter(categoria__iexact=categoria_nome).first()
            if not categoria_obj:
                categoria_obj = Categoria.objects.create(categoria=categoria_nome)
            instance.categoria = categoria_obj

        if modelo_nome:
            categoria_obj = instance.categoria
            modelo_obj = Modelo.objects.filter(modelo__iexact=modelo_nome, categoria=categoria_obj).first()
            if not modelo_obj:
                modelo_obj = Modelo.objects.create(modelo=modelo_nome, categoria=categoria_obj)
            instance.modelo = modelo_obj

        if commit:
            instance.save()

        return instance

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria']

    def clean_categoria(self):
        categoria = self.cleaned_data['categoria'].strip()
        if Categoria.objects.filter(categoria__iexact=categoria).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Esta categoria já está cadastrada.')
        return categoria

class ModeloForm(forms.ModelForm):
    categoria_text = forms.CharField(required=False, max_length=150, label='Categoria')

    class Meta:
        model = Modelo
        fields = ['modelo']

    def clean(self):
        cleaned_data = super().clean()
        modelo = (cleaned_data.get('modelo') or '').strip()
        categoria_nome = (cleaned_data.get('categoria_text') or '').strip()
        categoria = Categoria.objects.filter(categoria__iexact=categoria_nome).first() if categoria_nome else None
        if modelo and Modelo.objects.filter(modelo__iexact=modelo, categoria=categoria).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Este modelo já está cadastrado nesta categoria.')
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        categoria_nome = (self.cleaned_data.get('categoria_text') or '').strip()
        if categoria_nome:
            categoria_obj = Categoria.objects.filter(categoria__iexact=categoria_nome).first()
            if not categoria_obj:
                categoria_obj = Categoria.objects.create(categoria=categoria_nome)
            instance.categoria = categoria_obj

        if commit:
            instance.save()

        return instance
