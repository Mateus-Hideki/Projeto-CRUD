from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_admin
from .views import (
    inicio,
    lista_roupas,
    criar_roupa,
    editar_roupa,
    excluir_roupa,
    alterar_estoque,
    lista_modelos,
    criar_modelo,
    editar_modelo,
    excluir_modelo,
    lista_categorias,
    criar_categoria,
    editar_categoria,
    excluir_categoria,
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('login/', login_admin, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    path('roupas/', lista_roupas, name='lista_roupas'),
    path('roupas/novo/', criar_roupa, name='criar_roupa'),
    path('roupas/<int:id>/editar/', editar_roupa, name='editar_roupa'),
    path('roupas/<int:id>/excluir/', excluir_roupa, name='excluir_roupa'),
    path('roupas/<int:id>/alterar-estoque/', alterar_estoque, name='alterar_estoque'),
    path('modelos/', lista_modelos, name='lista_modelos'),
    path('modelos/novo/', criar_modelo, name='criar_modelo'),
    path('modelos/<int:id>/editar/', editar_modelo, name='editar_modelo'),
    path('modelos/<int:id>/excluir/', excluir_modelo, name='excluir_modelo'),
    path('categorias/', lista_categorias, name='lista_categorias'),
    path('categorias/novo/', criar_categoria, name='criar_categoria'),
    path('categorias/<int:id>/editar/', editar_categoria, name='editar_categoria'),
    path('categorias/<int:id>/excluir/', excluir_categoria, name='excluir_categoria'),
]