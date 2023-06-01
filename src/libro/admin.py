from django.contrib import admin
from .models import Libro
# Register your models here.

#admin.site.register(Libro)

class LibroAdmin(admin.ModelAdmin):
    """ Se define el atributo list_display para listar los autores
        Se Agrega opciones de búsqueda por nombre o apellido (list_search = search_fields)
        Se agrega la opción de filtrado por el field activo y nacionalidad (list_filter) """
    
    list_display = ["nombre","autor","editorial","activo"]
    

admin.site.register(Libro, LibroAdmin) # Registrar el modelo en el archivo admin.py


