# Exercício 4 - Servidor de Hora com Threads (TCP)

**Disciplina:** Redes de Computadores 2  
**Professor:** Alessandro Vivas Andrade  
**Participante:** Maicon Douglas  

## Objetivo

Implementar um servidor multithread TCP que forneça a hora atual no formato "HH:MM:SS" para múltiplos clientes simultaneamente.

## Estrutura

- `servidor.py`: Código do servidor que envia a hora para cada cliente conectado.
- `cliente.py`: Código do cliente que se conecta e exibe a hora recebida.

## Funcionalidades

- Servidor escutando na porta 7000.
- Cada conexão de cliente é atendida em uma thread separada.
- Envio da hora atual no formato "HH:MM:SS".
- Registro de log no servidor a cada requisição atendida.
- Tratamento de exceções para manter o servidor funcionando mesmo com falhas de clientes.

## Tecnologias

- Python 3.10+
- Sistema operacional: Linux (testado no Ubuntu)

## Como Executar

### 1. Iniciar o servidor

```bash
python3 servidor.py
2. Em outro terminal, iniciar o cliente
bash

python3 cliente.py
Exemplo
Servidor:


[*] Servidor de hora escutando na porta 7000...
[('127.0.0.1', 52844)] Solicitou hora: 11:32:18
Cliente:


Hora atual recebida do servidor: 11:32:18
