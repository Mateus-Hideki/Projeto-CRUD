from pathlib import Path
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import F
from django.http import FileResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from functools import wraps
from .forms import AlterarEstoqueForm, RoupaForm, CategoriaForm, ModeloForm
from .models import Roupa, Categoria, Modelo


def admin_required(view_func):
    @wraps(view_func)
    def wrapped(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
            return HttpResponseForbidden('Apenas o superusuário pode acessar o estoque.')
        return view_func(request, *args, **kwargs)

    return wrapped


def login_admin(request):
    if request.user.is_superuser:
        return redirect('inicio')

    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user and user.is_superuser:
            login(request, user)
            return redirect('inicio')
        form.add_error(None, 'Apenas o superusuário pode entrar neste sistema.')

    return render(request, 'core/login.html', {'form': form})


@login_required
def inicio(request):
    total_roupas = Roupa.objects.count()
    total_modelos = Modelo.objects.count()
    total_categorias = Categoria.objects.count()
    ultimas_roupas = Roupa.objects.select_related('categoria', 'modelo').order_by('-id')[:8]

    return render(request, 'core/inicio.html', {
        'total_roupas': total_roupas,
        'total_modelos': total_modelos,
        'total_categorias': total_categorias,
        'ultimas_roupas': ultimas_roupas,
    })


@login_required
def react_frontend(request):
    index_path = Path(settings.BASE_DIR.parent) / 'frontend' / 'dist' / 'index.html'

    if index_path.exists():
        return FileResponse(index_path.open('rb'), content_type='text/html')

    return render(request, 'core/inicio.html')

@login_required
def lista_roupas(request):
    roupas = Roupa.objects.all()
    return render(request, 'core/lista_roupas.html', {'roupas': roupas})

@admin_required
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


@admin_required
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


@admin_required
def excluir_roupa(request, id):
    roupa = get_object_or_404(Roupa, id=id)

    if request.method == 'POST':
        roupa.delete()
        messages.success(request, 'Peça removida com sucesso!')
        return redirect('lista_roupas')

    return render(request, 'core/lista_roupas.html', {'roupa': roupa})


@admin_required
def alterar_estoque(request, id):
    roupa = get_object_or_404(Roupa, id=id)
    form = AlterarEstoqueForm(request.POST or None, roupa=roupa)

    if request.method == 'POST' and form.is_valid():
        quantidade = form.cleaned_data['quantidade']
        if form.cleaned_data['operacao'] == 'adicionar':
            alterados = Roupa.objects.filter(id=roupa.id).update(quantidade=F('quantidade') + quantidade)
            mensagem = f'{quantidade} peça(s) adicionada(s) ao estoque.'
        else:
            alterados = Roupa.objects.filter(id=roupa.id, quantidade__gte=quantidade).update(quantidade=F('quantidade') - quantidade)
            mensagem = f'{quantidade} peça(s) retirada(s) do estoque.'

        if not alterados:
            form.add_error('quantidade', 'A quantidade informada deixaria o estoque negativo.')
        else:
            messages.success(request, mensagem)
            return redirect('lista_roupas')

    return render(request, 'core/form_alterar_estoque.html', {'form': form, 'roupa': roupa})


@login_required
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'core/lista_categorias.html', {'categorias': categorias})


@admin_required
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


@admin_required
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


@admin_required
def excluir_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoria removida com sucesso!')
        return redirect('lista_categorias')

    return render(request, 'core/lista_categorias.html', {'categoria': categoria})


@login_required
def lista_modelos(request):
    modelos = Modelo.objects.all()
    return render(request, 'core/lista_modelos.html', {'modelos': modelos})


@admin_required
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


@admin_required
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


@admin_required
def excluir_modelo(request, id):
    modelo = get_object_or_404(Modelo, id=id)

    if request.method == 'POST':
        modelo.delete()
        messages.success(request, 'Modelo removido com sucesso!')
        return redirect('lista_modelos')

    return render(request, 'core/lista_modelos.html', {'modelo': modelo})