# Exercício 1 - Cliente/Servidor TCP

**Disciplina:** Redes de Computadores 2  
**Professor:** Alessandro Vivas Andrade  
**Participante:** Maicon Douglas  

## Objetivo

Implementar um sistema Cliente/Servidor utilizando o protocolo TCP, com suporte a múltiplas conexões simultâneas, envio de mensagens e resposta do servidor.

## Estrutura

- `servidor.py`: Código do servidor TCP que aceita múltiplos clientes via threads.
- `cliente.py`: Código do cliente TCP que envia uma mensagem ao servidor e imprime a resposta.

## Funcionalidades

- Servidor escutando na porta 5000.
- Suporte a múltiplos clientes simultaneamente (uso de threads).
- Validação de mensagens vazias no cliente.
- Resposta automática do servidor: `"Mensagem recebida"`.
- Encerramento seguro da conexão.

## Tecnologias

- Python 3.10+
- Sistema operacional: Linux (testado no Ubuntu)

## Como Executar

### 1. Iniciar o servidor

```bash
python3 servidor.py
2. Iniciar o cliente (em outro terminal)
bash

python3 cliente.py
Digite uma mensagem e pressione Enter. O cliente exibirá a resposta recebida do servidor.

Exemplo
Cliente:

Digite sua mensagem: Olá, servidor!
Resposta do servidor: Mensagem recebida
Servidor:

[*] Servidor TCP escutando na porta 5000...
[+] Conexão estabelecida com ('127.0.0.1', 53120)
[('127.0.0.1', 53120)] Olá, servidor!
