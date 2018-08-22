from djongo import models

class Registro(models.Model):
    nombre = models.CharField(max_length=255, blank=False)
    servicio = models.CharField(max_length=255, blank=False)
    ciudad = models.CharField(max_length=255, blank=False)
    fecha = models.CharField(max_length=255, blank=False)
    total=models.IntegerField()
    def __str__(self):
        return self.nombre+" "+self.servicio+" "+self.ciudad+" "+self.fecha+" "+str(self.total)
