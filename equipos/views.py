from django.shortcuts import render

# Create your views here.
from .models import Equipo
from .utils import hacer_ping


def monitor(request):

    resultados = []

    for equipo in Equipo.objects.all():

        activo = hacer_ping(equipo.host)

        resultados.append({
            "nombre": equipo.nombre,
            "host": equipo.host,
            "descripcion": equipo.descripcion,
            "activo": activo
        })

    return render(
        request,
        "equipos/monitor.html",
        {"resultados": resultados}
    )
