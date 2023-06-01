from .models import Cliente
from django.views.generic import ListView,CreateView, UpdateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .forms import ClienteForm
from django.shortcuts import get_object_or_404 , redirect

# Create your views here.

class ListarClientes(ListView):
	model = Cliente
	template_name = "clientes/listar.html"
   
class CrearCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/crear.html"
    success_url = reverse_lazy('clientes:ListarClientes')
    
class EditarCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/editar.html' 
    success_url = reverse_lazy('clientes:ListarClientes')  

def activar_cliente(request, pk):
    empleado= get_object_or_404(Cliente, id = pk)
    empleado.activo = True
    empleado.save()
    return redirect(reverse_lazy('clientes:ListarClientes'))

def desactivar_cliente(request, id):
    empleado = get_object_or_404(Cliente, id = id)
    empleado.activo = False
    empleado.save()
    return redirect(reverse_lazy('clientes:ListarClientes'))