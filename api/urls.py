from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from cliente.views import ClienteListar, ClienteCreate, ClienteDelete
from producto.views import ProductoListar, ProductoCreate, ProductoDelete
from consumo.views import ConsumoListar, ConsumoCreate
from detalleconsumo.views import DetalleConsumoListar

urlpatterns = [
    path('clientes/listar', ClienteListar.as_view(), name='cliente_listar'),
    path('cliente/crear', ClienteCreate.as_view(), name='cliente_crear'),
    path('cliente/eliminar/<int:pk>', ClienteDelete.as_view(), name='cliente_eliminar'),
    path('productos/listar', ProductoListar.as_view(), name='producto_listar'),
    path('producto/crear', ProductoCreate.as_view(), name='producto_crear'),
    path('producto/eliminar/<int:pk>', ProductoDelete.as_view(), name='producto_eliminar'),
    path('consumo/listar', ConsumoListar.as_view(), name='consumo_listar'),
    path('consumo/crear', ConsumoCreate.as_view(), name='consumo_crear'),
    path('detalle-consumo/<slug:slug>', DetalleConsumoListar.as_view(), name='detalle'),
]

urlpatterns = format_suffix_patterns(urlpatterns)