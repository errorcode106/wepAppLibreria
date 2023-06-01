from django.contrib import admin
from .models import Pedido
from libro.models import Libro
# Register your models here.

#admin.site.register(Pedido)

class PedidoAdmin(admin.ModelAdmin):
    """ Se define el atributo list_display para listar los autores
        Se Agrega opciones de búsqueda por nombre o apellido (list_search = search_fields)
        Se agrega la opción de filtrado por el field activo y nacionalidad (list_filter) """
    
    list_display = ["numero_pedido","fecha_pedido","estado","libro","activo"]
    #list_filter = ["activo","dni"]
    #search_fields = ['mail', 'apellido']

admin.site.register(Pedido,PedidoAdmin) # Registrar el modelo en el archivo admin.py