# Participante: Maicon Douglas
# Exercício 4 - Servidor de Hora com Threads (TCP)
# Redes de Computadores 2

import socket
import threading
from datetime import datetime

def atender_cliente(conn, addr):
    """Atende um cliente e envia a hora atual"""
    try:
        hora = datetime.now().strftime("%H:%M:%S")
        print(f"[{addr}] Solicitou hora: {hora}")
        conn.sendall(hora.encode())
    except Exception as e:
        print(f"[!] Erro ao atender {addr}: {e}")
    finally:
        conn.close()

# Criação do socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 7000))
server.listen()

print("[*] Servidor de hora escutando na porta 7000...")

while True:
    try:
        conn, addr = server.accept()
        threading.Thread(target=atender_cliente, args=(conn, addr), daemon=True).start()
    except Exception as e:
        print(f"[!] Erro no servidor: {e}")
