from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response

from cliente.models import Cliente
from api.serializers import ClienteSerializer

# Create your views here.
class ClienteListar(generics.ListAPIView):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request, format=None):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)


class ClienteCreate(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request, *args, **kwargs):
        queryset = Cliente.objects.all()
        serializer = ClienteSerializer(queryset, many=True)
        return Response({'clientes': serializer.data})

    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('cliente_listar')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer