from django.shortcuts import render, redirect, get_object_or_404
from .models import Voluntario, Evento
from .forms import VoluntarioForm, EventoForm

def index(request):
    voluntarios = Voluntario.objects.all()
    eventos = Evento.objects.all()
    return render(request, 'gestion/index.html', {
        'voluntarios': voluntarios,
        'eventos': eventos
    })

def crear_voluntario(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VoluntarioForm()
    return render(request, 'gestion/form_generico.html', {'form': form, 'titulo': 'Crear Voluntario'})

def editar_voluntario(request, id):
    voluntario = get_object_or_404(Voluntario, id=id)
    if request.method == 'POST':
        form = VoluntarioForm(request.POST, instance=voluntario)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VoluntarioForm(instance=voluntario)
    return render(request, 'gestion/form_generico.html', {'form': form, 'titulo': 'Editar Voluntario'})

def eliminar_voluntario(request, id):
    voluntario = get_object_or_404(Voluntario, id=id)
    if request.method == 'POST':
        voluntario.delete()
        return redirect('index')
    return render(request, 'gestion/confirmar_eliminar.html', {'objeto': voluntario})

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventoForm()
    return render(request, 'gestion/form_generico.html', {'form': form, 'titulo': 'Crear Evento'})

def editar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'gestion/form_generico.html', {'form': form, 'titulo': 'Editar Evento'})

def eliminar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        evento.delete()
        return redirect('index')
    return render(request, 'gestion/confirmar_eliminar.html', {'objeto': evento})