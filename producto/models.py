from django.db import models
from cliente.models import Cliente

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    precio_unitario = models.IntegerField()

    def __str__(self):
        return self.nombre