from django.urls import path
from .views import inicio, lista_roupas, criar_roupa, excluir_roupa, lista_modelos, criar_modelo, excluir_modelo, lista_categorias, criar_categoria, excluir_categoria
urlpatterns = [
 path('', inicio, name='inicio'),
 path('roupas/', lista_roupas, name='lista_roupas'),
 path('roupas/novo/', criar_roupa, name='criar_roupa'),
 path('roupas/<int:id>/excluir/', excluir_roupa, name='excluir_roupa'),
 path('modelos/', lista_modelos, name='lista_modelos'),
 path('modelos/novo/', criar_modelo, name='criar_modelo'),
 path('modelos/<int:id>/excluir/', excluir_modelo, name='excluir_modelo'),
 path('categorias/', lista_categorias, name='lista_categorias'),
 path('categorias/novo/', criar_categoria, name='criar_categoria'),
 path('categorias/<int:id>/excluir/', excluir_categoria, name='excluir_categoria'),
]