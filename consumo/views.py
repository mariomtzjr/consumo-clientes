from django.shortcuts import render, redirect
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response

from api.serializers import ConsumoSerializer
from consumo.models import Consumo

# Create your views here.
class ConsumoListar(generics.ListAPIView):

    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer


class ConsumoCreate(generics.CreateAPIView):
    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer

    def get(self, request, *args, **kwargs):
        queryset = Consumo.objects.all()
        serializer = ConsumoSerializer(queryset, many=True)
        return Response({'consumos': serializer.data})

    def post(self, request):
        serializer = ConsumoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('consumo_crear')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)