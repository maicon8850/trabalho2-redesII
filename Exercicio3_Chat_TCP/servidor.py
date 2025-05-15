# Participante: Maicon Douglas
# Exercício 3 - Servidor TCP (Chat em rede)
# Redes de Computadores 2

import socket
import threading

clients = []

def encaminhar(mensagem, remetente):
    """Encaminha mensagem para todos os clientes, exceto o remetente"""
    for cliente in clients:
        if cliente != remetente:
            try:
                cliente.sendall(mensagem)
            except Exception as e:
                print(f"[!] Erro ao encaminhar mensagem: {e}")

def lidar_com_cliente(conn, addr):
    """Gerencia comunicação com um cliente"""
    print(f"[+] Cliente conectado: {addr}")
    clients.append(conn)
    try:
        while True:
            dados = conn.recv(1024)
            if not dados or dados.decode().lower() == "sair":
                break
            encaminhar(dados, conn)
    finally:
        print(f"[-] Cliente desconectado: {addr}")
        clients.remove(conn)
        conn.close()

# Criação do socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5001))
server.listen(2)

print("[*] Servidor de chat esperando até 2 clientes...")

while len(clients) < 2:
    conn, addr = server.accept()
    threading.Thread(target=lidar_com_cliente, args=(conn, addr), daemon=True).start()
