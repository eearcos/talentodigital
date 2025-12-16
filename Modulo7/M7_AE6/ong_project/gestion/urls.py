from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('voluntario/crear/', views.crear_voluntario, name='crear_voluntario'),
    path('voluntario/editar/<int:id>/', views.editar_voluntario, name='editar_voluntario'),
    path('voluntario/eliminar/<int:id>/', views.eliminar_voluntario, name='eliminar_voluntario'),

    path('evento/crear/', views.crear_evento, name='crear_evento'),
    path('evento/editar/<int:id>/', views.editar_evento, name='editar_evento'),
    path('evento/eliminar/<int:id>/', views.eliminar_evento, name='eliminar_evento'),
]