# Participante: Maicon Douglas
# Exercício 2 - Cliente UDP (Echo)
# Redes de Computadores 2

import socket

# Criação do socket UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    mensagem = input("Digite uma mensagem (ou 'sair' para encerrar): ").strip()

    if mensagem.lower() == "sair":
        print("Encerrando o cliente.")
        break

    if len(mensagem.encode()) > 65507:
        print("Mensagem muito longa (limite do UDP é 65507 bytes).")
        continue

    try:
        client.sendto(mensagem.encode(), ('localhost', 6000))
        client.settimeout(2.0)  # Timeout de 2 segundos para resposta
        resposta, _ = client.recvfrom(65535)
        print("Eco do servidor:", resposta.decode())
    except socket.timeout:
        print("⚠️ Tempo de resposta esgotado (timeout).")
    except Exception as e:
        print(f"[!] Erro: {e}")
