import subprocess

def hacer_ping(ip):
    """
    Linux:
    -c 1 = 1 paquete
    -W 1 = espera máxima 1 segundo
    """

    resultado = subprocess.run(
        ["ping", "-c", "1", "-W", "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return resultado.returncode == 0
