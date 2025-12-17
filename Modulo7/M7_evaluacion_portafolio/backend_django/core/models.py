from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Curso")
    precio = models.IntegerField(verbose_name="Precio (CLP)")
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    curso_interes = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso Inscrito")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"