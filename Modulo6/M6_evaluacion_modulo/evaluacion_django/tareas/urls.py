from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Rutas de Tareas
    path('', views.lista_tareas, name='lista_tareas'),
    path('tarea/<int:tarea_id>/', views.detalle_tarea, name='detalle_tarea'),
    path('agregar/', views.agregar_tarea, name='agregar_tarea'),
    path('eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
    
    # Rutas de Autenticación
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]