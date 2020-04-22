from rest_framework import serializers
from cliente.models import Cliente
from producto.models import Producto
from consumo.models import Consumo
from detalleconsumo.models import DetalleConsumo

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class ConsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumo
        fields = '__all__'
    
class DetalleConsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleConsumo
        fields = '__all__'