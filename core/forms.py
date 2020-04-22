from django import forms
from django.utils.text import slugify


class ConsultaForm(forms.Form):
    nombre_cliente = forms.CharField(max_length=100)
    apellido_cliente = forms.CharField(max_length=100)