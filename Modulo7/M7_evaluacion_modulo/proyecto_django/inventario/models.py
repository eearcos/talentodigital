from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    # Relación 1 a Muchos
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    # Relación Muchos a Muchos
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)

    def __str__(self):
        return self.nombre

class DetalleProducto(models.Model):
    # Relación 1 a 1
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
    dimensiones = models.CharField(max_length=100, help_text="Ej: 10x20x30 cm")
    peso = models.DecimalField(max_digits=6, decimal_places=2, help_text="Peso en Kg")

    def __str__(self):
        return f"Detalles de {self.producto.nombre}"