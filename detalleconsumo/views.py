from django.shortcuts import render, redirect
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response

from api.serializers import DetalleConsumoSerializer
from detalleconsumo.models import DetalleConsumo
from cliente.models import Cliente
from consumo.models import Consumo

# Create your views here.
class DetalleConsumoListar(generics.ListAPIView):

    queryset = DetalleConsumo.objects.all()
    serializer_class = DetalleConsumoSerializer
    slug_field = 'slug'  

    def get(self, request, *args, **kwargs):
        nombre_cliente = self.kwargs.get('slug', None)
        cliente = Cliente.objects.get(slug=nombre_cliente)
        productos = Consumo.objects.filter(cliente=cliente.id)
        pago_total = 0
        detalle = {
            "cliente": " ",
            "productos": [],
            "total_pagado": " "
        }
        products = []

        for consumo in productos:
            pago_total += consumo.producto.precio_unitario
            products.append({
                'producto': str(consumo.producto.nombre),
                'descripcion': str(consumo.producto.descripcion),
                'precio_unitario': int(consumo.producto.precio_unitario),
            })
        
        detalle['cliente'] = str(cliente)
        detalle['productos'] = products
        detalle['total_pagado'] = pago_total

        return Response(detalle)
        