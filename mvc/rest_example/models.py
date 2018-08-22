from django.db import models

# Create your models here.


class Servicio(models.Model):
    nombre = models.CharField(max_length=200)
    fecha=models.DateField()
    direccion=models.CharField(max_length=500)
    def __str__(self):
        return self.nombre +" "+str(self.fecha)+" "+self.direccion

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    servicios=models.ManyToManyField(Servicio)
    def __str__(self):
        return self.nombre
