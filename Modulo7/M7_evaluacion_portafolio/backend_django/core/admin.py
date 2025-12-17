from django.contrib import admin
from .models import Curso, Estudiante

# Esto permite gestionar los datos desde /admin
admin.site.register(Curso)
admin.site.register(Estudiante)