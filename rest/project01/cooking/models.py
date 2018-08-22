#from django.db import models
from djongo import models
# Create your models here.

"""
class Servicio(models.Model):
    nombre = models.CharField(max_length=200)        
    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre

"""
class Usuario(models.Model):     
    nombre = models.CharField(max_length=200)
    servicio = models.CharField(max_length=200) 
    ciudad = models.CharField(max_length=200)
    fecha = models.DateField('fecha en la que adquirio el servicio')    
    #objects = models.Manager()
    def __str__(self):
        return self.nombre
