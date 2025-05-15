# Participante: Maicon Douglas
# Exercício 2 - Servidor UDP (Echo)
# Redes de Computadores 2

import socket

# Criação do socket UDP
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('0.0.0.0', 6000))

print("[*] Servidor UDP escutando na porta 6000...")

while True:
    try:
        data, addr = server.recvfrom(65535)
        print(f"[{addr}] {data.decode()}")
        server.sendto(data, addr)  # Eco da mensagem
    except Exception as e:
        print(f"[!] Erro: {e}")
