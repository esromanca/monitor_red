import socket
import subprocess


def ping_host(host):

    resultado = subprocess.run(
        ["ping", "-c", "1", host],
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


def scan_ports(host, ports):

    abiertos = []

    for port in ports:

        if scan_port(host, port):
            abiertos.append(port)

    return abiertos
