from django.db import models

class Producto(models.Model):
    # db_index=True cumple con el punto 5 (Índices)
    nombre = models.CharField(max_length=100, db_index=True) 
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} (${self.precio})"