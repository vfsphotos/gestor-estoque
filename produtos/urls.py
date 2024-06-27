from django.urls import path

from .views import (
    adicionar_local,
    home,
    listar_locais,
)

urlpatterns = [
    path('', home, name='home'),
    path('locais/', listar_locais, name='listar_locais'),
    path('locais/adicionar/', adicionar_local, name='adicionar_local'),
]
