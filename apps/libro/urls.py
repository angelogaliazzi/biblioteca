from django.urls import path
from .views import *

urlpatterns = [
    path('', Inicio.as_view(), name='index'),
    path('crear_autor/', crearautor, name='crear_autor'),
    path('listar_autor/', ListadoAutor.as_view(), name='listar_autor'),
    path('editar_autor/<int:id>', editarautor, name='editar_autor'),
    path('eliminar_autor/<int:id>', eliminarautor, name='eliminar_autor')
]
