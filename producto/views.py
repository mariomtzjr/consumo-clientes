from django.shortcuts import render, redirect
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response

from producto.models import Producto
from api.serializers import ProductoSerializer

# Create your views here.
class ProductoListar(generics.ListAPIView):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get(self, request, format=None):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)


class ProductoCreate(generics.CreateAPIView):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get(self, request, *args, **kwargs):
        queryset = Producto.objects.all()
        serializer = ProductoSerializer(queryset, many=True)
        return Response({'productos': serializer.data})

    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('producto_crear')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer