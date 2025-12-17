from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Curso
from .forms import EstudianteForm

# Vista Pública: Muestra datos de la BD (Dinámico)
def home(request):
    cursos = Curso.objects.all()
    return render(request, 'core/home.html', {'cursos': cursos})

# Vista Privada: Requiere Login (Seguridad)
@login_required
def inscribir_alumno(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EstudianteForm()
    return render(request, 'core/registro.html', {'form': form})