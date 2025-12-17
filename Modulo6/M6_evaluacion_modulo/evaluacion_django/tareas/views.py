from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import Http404
from .forms import TareaForm

# --- BASE DE DATOS EN MEMORIA ---
# Estructura: {'id': int, 'titulo': str, 'descripcion': str, 'usuario': str}
TAREAS = []

# --- VISTAS DE AUTENTICACIÓN ---

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loguear automáticamente tras registro
            return redirect('lista_tareas')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

# --- VISTAS DE TAREAS ---

@login_required
def lista_tareas(request):
    # Filtramos las tareas para mostrar solo las del usuario actual
    mis_tareas = [t for t in TAREAS if t['usuario'] == request.user.username]
    return render(request, 'tareas/lista.html', {'tareas': mis_tareas})

@login_required
def agregar_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            nueva_tarea = {
                'id': len(TAREAS) + 1, # ID simple basado en longitud
                'titulo': form.cleaned_data['titulo'],
                'descripcion': form.cleaned_data['descripcion'],
                'usuario': request.user.username # Asignamos dueño
            }
            TAREAS.append(nueva_tarea)
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'tareas/agregar.html', {'form': form})

@login_required
def detalle_tarea(request, tarea_id):
    # Buscar tarea por ID y asegurar que pertenezca al usuario
    tarea = next((t for t in TAREAS if t['id'] == tarea_id and t['usuario'] == request.user.username), None)
    
    if not tarea:
        raise Http404("Tarea no encontrada o no tienes permiso.")
        
    return render(request, 'tareas/detalle.html', {'tarea': tarea})

@login_required
def eliminar_tarea(request, tarea_id):
    global TAREAS
    # Reconstruimos la lista excluyendo la tarea seleccionada (si pertenece al usuario)
    TAREAS = [t for t in TAREAS if not (t['id'] == tarea_id and t['usuario'] == request.user.username)]
    return redirect('lista_tareas')