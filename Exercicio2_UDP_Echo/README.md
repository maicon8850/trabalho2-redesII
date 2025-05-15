# Exercício 2 - Servidor Echo UDP

**Disciplina:** Redes de Computadores 2  
**Professor:** Alessandro Vivas Andrade  
**Participante:** Maicon Douglas  

## Objetivo

Implementar um servidor e cliente utilizando o protocolo UDP, no qual as mensagens enviadas pelo cliente são devolvidas pelo servidor (eco).

## Estrutura

- `servidor.py`: Código do servidor UDP que recebe e devolve mensagens.
- `cliente.py`: Código do cliente UDP que envia mensagens e recebe as respostas.

## Funcionalidades

- Servidor escutando na porta 6000.
- Cliente envia mensagens continuamente até digitar `"sair"`.
- Eco das mensagens do cliente é devolvido pelo servidor.
- Validação de tamanho da mensagem (limite do UDP: 65507 bytes).
- Tratamento de erros e timeout (2 segundos).

## Tecnologias

- Python 3.10+
- Sistema operacional: Linux (testado no Ubuntu)

## Como Executar

### 1. Iniciar o servidor

```bash
python3 servidor.py
2. Em outro terminal, iniciar o cliente

python3 cliente.py
Digite uma mensagem e pressione Enter. O cliente exibirá o eco enviado pelo servidor.

Exemplo
Cliente:


Digite uma mensagem (ou 'sair' para encerrar): Olá servidor UDP!
Eco do servidor: Olá servidor UDP!
Servidor:

[*] Servidor UDP escutando na porta 6000...
[('127.0.0.1', 59452)] Olá servidor UDP!
