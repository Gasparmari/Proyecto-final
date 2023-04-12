from django.db import models

# Create your models here.


class Banda(models.Model):
    nombre = models.CharField(max_length=20)
    origen = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=1500)
    integrantes = models.CharField(max_length=50, default='')
    anio_creacion= models.IntegerField( default='some string')
    
    def __str__(self):
        return f'{self.id} - {self.nombre}'
    