from pathlib import Path
from django.conf import settings
from django.contrib import messages
from django.http import FileResponse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import RoupaForm, CategoriaForm, ModeloForm
from .models import Roupa, Categoria, Modelo


def inicio(request):
    total_roupas = Roupa.objects.count()
    total_modelos = Modelo.objects.count()
    total_categorias = Categoria.objects.count()
    ultimas_roupas = Roupa.objects.select_related('categoria', 'modelo').order_by('-id')[:5]

    return render(request, 'core/inicio.html', {
        'total_roupas': total_roupas,
        'total_modelos': total_modelos,
        'total_categorias': total_categorias,
        'ultimas_roupas': ultimas_roupas,
    })


def react_frontend(request):
    index_path = Path(settings.BASE_DIR.parent) / 'frontend' / 'dist' / 'index.html'

    if index_path.exists():
        return FileResponse(index_path.open('rb'), content_type='text/html')

    return render(request, 'core/inicio.html')

def lista_roupas(request):
    roupas = Roupa.objects.all()
    return render(request, 'core/lista_roupas.html', {'roupas': roupas})

def criar_roupa(request):
    if request.method == 'POST':
        form = RoupaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Peça cadastrada com sucesso!')
            return redirect('lista_roupas')
        messages.error(request, 'Não foi possível cadastrar a peça. Verifique os campos.')
    else:
        form = RoupaForm()

    return render(request, 'core/form_roupa.html', {'form': form})


def editar_roupa(request, id):
    roupa = get_object_or_404(Roupa, id=id)

    if request.method == 'POST':
        form = RoupaForm(request.POST, instance=roupa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Peça atualizada com sucesso!')
            return redirect('lista_roupas')
        messages.error(request, 'Não foi possível atualizar a peça. Verifique os campos.')
    else:
        initial_data = {
            'categoria_text': roupa.categoria.categoria if roupa.categoria else '',
            'modelo_text': roupa.modelo.modelo if roupa.modelo else '',
        }
        form = RoupaForm(instance=roupa, initial=initial_data)

    return render(request, 'core/form_roupa.html', {'form': form, 'editando': True})


def excluir_roupa(request, id):
    roupa = get_object_or_404(Roupa, id=id)

    if request.method == 'POST':
        roupa.delete()
        messages.success(request, 'Peça removida com sucesso!')
        return redirect('lista_roupas')

    return render(request, 'core/lista_roupas.html', {'roupa': roupa})


def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'core/lista_categorias.html', {'categorias': categorias})


def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria cadastrada com sucesso!')
            return redirect('lista_categorias')
        messages.error(request, 'Não foi possível cadastrar a categoria. Verifique os campos.')

    else:
        form = CategoriaForm()

    return render(request, 'core/form_categoria.html', {'form': form})


def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria atualizada com sucesso!')
            return redirect('lista_categorias')
        messages.error(request, 'Não foi possível atualizar a categoria. Verifique os campos.')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'core/form_categoria.html', {'form': form, 'editando': True})


def excluir_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoria removida com sucesso!')
        return redirect('lista_categorias')

    return render(request, 'core/lista_categorias.html', {'categoria': categoria})


def lista_modelos(request):
    modelos = Modelo.objects.all()
    return render(request, 'core/lista_modelos.html', {'modelos': modelos})


def criar_modelo(request):
    if request.method == 'POST':
        form = ModeloForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Modelo cadastrado com sucesso!')
            return redirect('lista_modelos')
        messages.error(request, 'Não foi possível cadastrar o modelo. Verifique os campos.')

    else:
        form = ModeloForm()

    return render(request, 'core/form_modelo.html', {'form': form})


def editar_modelo(request, id):
    modelo = get_object_or_404(Modelo, id=id)

    if request.method == 'POST':
        form = ModeloForm(request.POST, instance=modelo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modelo atualizado com sucesso!')
            return redirect('lista_modelos')
        messages.error(request, 'Não foi possível atualizar o modelo. Verifique os campos.')
    else:
        initial_data = {'categoria_text': modelo.categoria.categoria if modelo.categoria else ''}
        form = ModeloForm(instance=modelo, initial=initial_data)

    return render(request, 'core/form_modelo.html', {'form': form, 'editando': True})


def excluir_modelo(request, id):
    modelo = get_object_or_404(Modelo, id=id)

    if request.method == 'POST':
        modelo.delete()
        messages.success(request, 'Modelo removido com sucesso!')
        return redirect('lista_modelos')

    return render(request, 'core/lista_modelos.html', {'modelo': modelo})