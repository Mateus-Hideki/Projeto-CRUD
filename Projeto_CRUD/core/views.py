from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import RoupaForm, CategoriaForm, ModeloForm
from .models import Roupa, Categoria, Modelo

def inicio(request):
    return render(request, 'core/inicio.html')

def lista_roupas(request):
    roupas = Roupa.objects.all()
    return render(request, 'core/lista_roupas.html', {'roupas': roupas})

def criar_roupa(request):
    if request.method == 'POST':
        form = RoupaForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('lista_roupas')
    
    else:
        form = RoupaForm()

    return render(request, 'core/form_roupa.html', {'form': form})

def excluir_roupa(request, id):
    roupa = get_object_or_404(Roupa, id=id)

    if request.method == 'POST':
        roupa.delete()
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
            return redirect('lista_categorias')
    
    else:
        form = CategoriaForm()

    return render(request, 'core/form_categoria.html', {'form': form})

def excluir_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        categoria.delete()
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
            return redirect('lista_modelos')
    
    else:
        form = ModeloForm()

    return render(request, 'core/form_modelo.html', {'form': form})

def excluir_modelo(request, id):
    modelo = get_object_or_404(Modelo, id=id)

    if request.method == 'POST':
        modelo.delete()
        return redirect('lista_modelos')

    return render(request, 'core/lista_modelos.html', {'modelo': modelo})