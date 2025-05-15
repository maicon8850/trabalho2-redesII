# Participante: Maicon Douglas
# Exercício 3 - Cliente TCP (Chat em rede)
# Redes de Computadores 2

import socket
import threading

def receber(sock):
    """Recebe mensagens do servidor e exibe no console"""
    while True:
        try:
            msg = sock.recv(1024)
            if not msg:
                break
            print("\nMensagem recebida:", msg.decode())
        except Exception as e:
            print(f"[!] Erro ao receber mensagem: {e}")
            break

# Conecta ao servidor
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 5001))

# Inicia thread para receber mensagens
threading.Thread(target=receber, args=(cliente,), daemon=True).start()

# Envia mensagens até digitar 'sair'
while True:
    texto = input("Você: ").strip()
    if texto.lower() == "sair":
        cliente.sendall(texto.encode())
        break
    cliente.sendall(texto.encode())

cliente.close()
