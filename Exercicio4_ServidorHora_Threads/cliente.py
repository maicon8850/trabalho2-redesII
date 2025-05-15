# Participante: Maicon Douglas
# Exercício 4 - Cliente TCP (Servidor de Hora)
# Redes de Computadores 2

import socket

try:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 7000))

    hora = cliente.recv(1024).decode()
    print("Hora atual recebida do servidor:", hora)

except Exception as e:
    print(f"[!] Erro ao conectar: {e}")
finally:
    cliente.close()
