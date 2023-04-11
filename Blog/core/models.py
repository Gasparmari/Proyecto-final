from django.db import models

# Create your models here.


class Banda(models.Model):
    nombre = models.CharField(max_length=20)
    origen = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=200)
    
    def __str__(self):
        return f'{self.id} - {self.nombre}'
    