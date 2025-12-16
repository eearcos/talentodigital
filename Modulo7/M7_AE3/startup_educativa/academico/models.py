from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    def __str__(self): return f"{self.nombre} {self.apellido}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    def __str__(self): return f"{self.nombre} {self.apellido}"

class Perfil(models.Model):
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE)
    biografia = models.TextField(blank=True)
    foto_perfil = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    web_redes_sociales = models.URLField(blank=True)

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='cursos')
    estudiantes = models.ManyToManyField(Estudiante, through='Inscripcion', related_name='cursos')
    def __str__(self): return f"{self.nombre}"

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=3, choices=[('ACT', 'Activo'), ('FIN', 'Finalizado')], default='ACT')
    nota_final = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)