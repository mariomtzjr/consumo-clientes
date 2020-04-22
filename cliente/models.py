from django.db import models
from django.utils.text import slugify

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion =  models.CharField(max_length=150)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    slug = models.SlugField(max_length=150, default=None, null=True, blank=True)

    def __str__(self):
        return self.nombre + " " + self.apellido
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre + " " + self.apellido)
        return super(Cliente, self).save(*args, **kwargs) 