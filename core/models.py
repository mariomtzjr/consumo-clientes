from django.db import models

# Create your models here.
class Consulta(models.Model):
    nombre_cliente = models.CharField(max_length=100)
