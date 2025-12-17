"""
URL configuration for gestion_academica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# 1. Importamos las vistas de autenticación de Django (Login/Logout)
from django.contrib.auth import views as auth_views
# 2. Importamos tus vistas desde la app 'core'
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # --- AUTENTICACIÓN (LOGIN / LOGOUT) ---
    # Como no tienes vista de login en views.py, usamos la de Django
    # pero le decimos que use TU template (core/login.html)
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    # Al salir, Django redirigirá al home automáticamente si está configurado en settings
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # --- TUS RUTAS (VISTAS) ---
    path('', views.home, name='home'),

    # --- LA SOLUCIÓN AL ERROR ---
    # Aquí hacemos el "puente".
    # Aunque tu función se llama 'inscribir_alumno', le ponemos nombre='inscripcion'
    # para que el template {% url 'inscripcion' %} la encuentre.
    path('inscripcion/', views.inscribir_alumno, name='inscripcion'),
    
    # Agregamos también 'registro' apuntando a lo mismo por si algún botón lo llama así
    path('registro/', views.inscribir_alumno, name='registro'),
]