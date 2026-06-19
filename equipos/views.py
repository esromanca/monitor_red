from django.shortcuts import render

from .models import Equipo
from .utils import ping_host
from .utils import scan_ports


def estado_equipos(request):

    resultados = []

    for equipo in Equipo.objects.all():

        activo = ping_host(
            equipo.host
        )

        abiertos = []

        if activo:

            puertos = [
                int(x.strip())
                for x in equipo.puertos.split(",")
                if x.strip()
            ]

            abiertos = scan_ports(
                equipo.host,
                puertos
            )

        resultados.append({

            "nombre": equipo.nombre,

            "host": equipo.host,

            "descripcion": equipo.descripcion,

            "activo": activo,

            "puertos": abiertos

        })

    return render(
        request,
        "equipos/monitor.html",
        {
            "resultados": resultados
        }
    )
