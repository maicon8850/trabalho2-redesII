# Participantes: Maicon Douglas
# Servidor TCP - Exercício 1

import socket
import threading

def handle_client(conn, addr):
    print(f"[+] Conexão estabelecida com {addr}")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"[{addr}] {data}")
        conn.sendall("Mensagem recebida".encode())
    conn.close()

# Cria o socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5000))  # Escuta em todas as interfaces na porta 5000
server.listen()

print("[*] Servidor TCP escutando na porta 5000...")
while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()
