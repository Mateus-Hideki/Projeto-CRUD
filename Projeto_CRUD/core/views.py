from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import RoupaForm
from .models import Roupa

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
