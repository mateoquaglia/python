import socket

ip = input("ingrese la ip a escanear: ")

for puerto in range(1, 65535):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    resultado = sock.connect_ex((ip, puerto))

    if resultado == 0:
        print("Puerto abierto: " + str(puerto))
        sock.close()
    else:
        print("Puerto cerrado: " + str(puerto))