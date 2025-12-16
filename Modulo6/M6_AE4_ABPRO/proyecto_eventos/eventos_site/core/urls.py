from django.urls import path
from .views import ListaEventos, CrearEvento, EditarEvento, EliminarEvento

urlpatterns = [
    path('', ListaEventos.as_view(), name='lista_eventos'),
    path('crear/', CrearEvento.as_view(), name='crear_evento'),
    path('editar/<int:pk>/', EditarEvento.as_view(), name='editar_evento'),
    path('eliminar/<int:pk>/', EliminarEvento.as_view(), name='eliminar_evento'),
]