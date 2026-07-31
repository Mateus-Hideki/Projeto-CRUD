from django.urls import path
from .views import inicio, lista_roupas, criar_roupa, excluir_roupa
urlpatterns = [
 path('', inicio, name='inicio'),
 path('roupas/', lista_roupas, name='lista_roupas'),
 path('roupas/novo/', criar_roupa, name='criar_roupa'),
 path('roupas/<int:id>/excluir/', excluir_roupa, name='excluir_roupa'),
]