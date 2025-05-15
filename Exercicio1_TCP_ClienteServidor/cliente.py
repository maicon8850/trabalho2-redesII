# Participantes: Maicon Douglas
# Cliente TCP - Exercício 1

import socket

# Cria o socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5000))  # Conecta ao servidor local

# Envia mensagem para o servidor
mensagem = input("Digite sua mensagem: ").strip()
if mensagem:
    client.sendall(mensagem.encode())
    resposta = client.recv(1024).decode()
    print("Resposta do servidor:", resposta)
else:
    print("Mensagem vazia não enviada!")

client.close()
