from django.db import models


class Equipo(models.Model):

    nombre = models.CharField(
        max_length=100
    )

    host = models.CharField(
        max_length=255,
        help_text="Dirección IP o nombre DNS"
    )

    descripcion = models.TextField(
        blank=True
    )

    puertos = models.CharField(
        max_length=200,
        default="22,53,80,443,44444",
        help_text="Lista de puertos separados por comas"
    )

    def __str__(self):
        return f"{self.nombre} ({self.host})"
