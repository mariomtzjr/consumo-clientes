from django.db import models
from django.utils.text import slugify
from consumo.models import Consumo
from producto.models import Producto

# Create your models here.
class DetalleConsumo(models.Model):
    consumo = models.ForeignKey(Consumo, on_delete=models.SET_NULL, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.IntegerField()

        