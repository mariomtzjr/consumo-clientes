from django.db import models
from cliente.models import Cliente
from producto.models import Producto

# Create your models here.
class Consumo(models.Model): 
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL,  blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_consumo = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField()