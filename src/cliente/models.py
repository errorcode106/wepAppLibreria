from django.db import models
from django.urls import reverse

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=8)
    mail = models.CharField(max_length=50)
    activo = models.BooleanField(default= True)

    def __str__(self):
        return F"{self.nombre.upper()}, {self.apellido.title()}, mail: {self.mail}"
    
    class Meta:
        ordering = ["apellido","nombre","mail"]
    
    def get_absolute_url(self):
        return reverse("clientes:ListarClientes", kwargs={"pk": self.pk})
    