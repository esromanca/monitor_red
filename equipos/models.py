from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    host = models.CharField(max_length=255, unique=True)
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre
