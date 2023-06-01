from django.urls import path
from .views import (ListarClientes,
                    CrearCliente,
                    EditarCliente,
                    activar_cliente,
                    desactivar_cliente,
                   )

app_name = "clientes"


urlpatterns = [
    path("",ListarClientes.as_view(), name="ListarClientes"),
    path('crear',CrearCliente.as_view(), name= 'CrearCliente' ),
    path("modificar/<int:pk>",EditarCliente.as_view(), name = "EditarCliente"),
    path('activar/<pk>', activar_cliente, name= 'activar_cliente'),
    path('desactivar/<int:id>', desactivar_cliente, name= 'desactivar_cliente'),
]

