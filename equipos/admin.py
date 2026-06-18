from django.contrib import admin

# Register your models here.
from .models import Equipo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "host", "descripcion")
    search_fields = ("nombre", "host")
