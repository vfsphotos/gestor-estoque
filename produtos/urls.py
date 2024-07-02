from django.urls import path

from .views import (
    adicionar_embalagem,
    adicionar_local,
    editar_embalagem,
    editar_local,
    excluir_embalagem,
    excluir_local,
    home,
    listar_embalagens,
    listar_locais,
)

urlpatterns = [
    path('', home, name='home'),
    path('locais/', listar_locais, name='listar_locais'),
    path('locais/adicionar/', adicionar_local, name='adicionar_local'),
    path('embalagens/', listar_embalagens, name='listar_embalagens'),
    path('embalagens/adicionar/', adicionar_embalagem, name='adicionar_embalagem'),
    path('locais/<int:id>/editar', editar_local, name='editar_local'),
    path('locais/<int:id>/excluir', excluir_local, name='excluir_local'),
    path('embalagem/<int:id>/editar', editar_embalagem, name='editar_embalagem'),
    path('embalagem/<int:id>/excluir', excluir_embalagem, name='excluir_embalagem'),
]
