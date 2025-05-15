# Exercício 3 - Chat em Rede (TCP)

**Disciplina:** Redes de Computadores 2  
**Professor:** Alessandro Vivas Andrade  
**Participante:** Maicon Douglas  

## Objetivo

Implementar um sistema de chat em tempo real utilizando o protocolo TCP, permitindo a comunicação bidirecional entre dois usuários.

## Estrutura

- `servidor.py`: Código do servidor que aceita 2 clientes e transmite mensagens entre eles.
- `cliente.py`: Código do cliente que envia e recebe mensagens simultaneamente.

## Funcionalidades

- Comunicação bidirecional entre dois clientes.
- Transmissão de mensagens em tempo real com threads.
- Comando `"sair"` para encerrar o chat.
- Servidor aceita no máximo 2 conexões.

## Tecnologias

- Python 3.10+
- Sistema operacional: Linux (testado no Ubuntu)

## Como Executar

### 1. Iniciar o servidor

```bash
python3 servidor.py
O servidor ficará aguardando dois clientes se conectarem.

2. Em dois terminais diferentes, iniciar dois clientes
bash

python3 cliente.py
Digite mensagens para o outro usuário. Digite sair para encerrar o chat.

Exemplo
Cliente 1:

Você: Olá, tudo bem?
Mensagem recebida: Tudo sim! E você?
Cliente 2:

Você: Tudo sim! E você?
Mensagem recebida: Olá, tudo bem?
