from django.db import models

# Create your models here.

class Libro (models.Model):
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=30)
    editorial = models.CharField(max_length=30)
    activo = models.BooleanField(default= True)
