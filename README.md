# Consumo-clientes

### Desarrollo de API REST

#### Descripción
La api permite obtener el detalle de consumo de un cliente, 
mostrando los productos adquiridos(consumidos), el precio unitario
de cada producto y el pago total por todos los productos.

#### Endpoints de la API
- /clientes/listar: Listado de los clientes almacenados en la Base de Datos
- /cliente/crear: Permite crear un cliente
- /cliente/eliminar/<int:pk>: Permite eliminar un cliente con id = pk
- /productos/listar: Listado de los productos almacenados en la BD
- /producto/crear: Permite crear un producto
- /producto/eliminar/<int:pk>: Permite eliminar un producto con id = pk
- /consumo/listar: Listado de los consumos (cliente, productos y cantidad)
- /consumo/crear: Permite realizar un consumo (venta), seleccionando producto y cliente.
- /detalle-consumo/<slug:slug>: Muestra el detalle de consumo de cada cliente proporcionando
de la forma <nombre-apellido>, el campo slug es generado automáticamente después de introducir
el nombre y apellido desde el formulario.
- /consultar: Muestra un formulario para introducir nombre y apellido a consultar

#### ScreenShots
##### Vista del formulario
![Formulario](/capturas/formulario.png)

##### Vista del formulario con datos
![Formulario](/capturas/formulario_datos.png)

##### Vista de la respuesta
![Formulario](/capturas/respuesta_formulario.png)

##### Vista de usuario no encontrado
![Formulario](/capturas/usuario_no_existe.png)
