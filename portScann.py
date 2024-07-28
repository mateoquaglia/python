import socket

def escanear_puerto(ip, puerto):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        resultado = sock.connect_ex((ip, puerto))
        if resultado == 0:
            print(f"Puerto abierto: {puerto}")
    except socket.error:
        print(f"Error al conectar al puerto: {puerto}")
    finally:
        sock.close()

def main():
    ip = input("Ingrese la IP a escanear: ")
    puerto_inicio = int(input("Ingrese el puerto de inicio: "))
    puerto_fin = int(input("Ingrese el puerto final: "))

    for puerto in range(puerto_inicio, puerto_fin + 1):
        escanear_puerto(ip, puerto)

if __name__ == "__main__":
    main() 
