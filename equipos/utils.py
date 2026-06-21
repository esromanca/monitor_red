import socket
import subprocess
from concurrent.futures import ThreadPoolExecutor
def ping_host(host):

    resultado = subprocess.run(
        ["ping", "-c", "1", "-W", "1", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return resultado.returncode == 0

def scan_port(host, port):

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    sock.settimeout(1)

    try:
        return sock.connect_ex((host, port)) == 0

    finally:
        sock.close()


def scan_ports_antiguo(host, ports):

    abiertos = []

    for port in ports:

        if scan_port(host, port):
            abiertos.append(port)

    return abiertos

def scan_ports(host, ports):

    abiertos = []

    with ThreadPoolExecutor(max_workers=100) as executor:

        resultados = executor.map(
            lambda port: (port, scan_port(host, port)),
            ports
        )

        for port, abierto in resultados:

            if abierto:
                abiertos.append(port)

    return abiertos
