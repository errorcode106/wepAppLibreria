from django.contrib import admin
from .models import Cliente
# Register your models here.

#admin.site.register(Cliente)

class ClienteAdmin(admin.ModelAdmin):
    """ Se define el atributo list_display para listar los autores
        Se Agrega opciones de búsqueda por nombre o apellido (list_search = search_fields)
        Se agrega la opción de filtrado por el field activo y nacionalidad (list_filter) """
    
    list_display = ["nombre","apellido","dni","mail","activo"]
    list_filter = ["activo","dni"]
    search_fields = ['mail', 'apellido']

admin.site.register(Cliente, ClienteAdmin) # Registrar el modelo en el archivo admin.py
