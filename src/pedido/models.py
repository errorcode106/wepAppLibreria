from django.db import models
from libro.models import Libro
from cliente.models import Cliente
from datetime import datetime


# Create your models here.
class Pedido(models.Model):
    numero_pedido = models.CharField(max_length=8)
    fecha_pedido = models.DateTimeField(default=datetime.now)
    estado = models.CharField(max_length=20)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
