# Sistema Bancário Orientado a Objetos - Completo

Este projeto apresenta uma versão avançada de um sistema bancário, utilizando Programação Orientada a Objetos (POO) e boas práticas de software.

## Funcionalidades

- Cadastro de clientes com validação de CPF e senha
- Criação de contas (corrente e poupança) associadas a clientes
- Autenticação de clientes para operar contas
- Depósito, saque, extrato e histórico de transações
- Persistência dos dados em arquivo JSON
- Listagem de clientes e suas contas
- Interface de linha de comando (CLI) intuitiva
- Estrutura pronta para testes automatizados

## Como executar

1. Certifique-se de ter Python 3 instalado.
2. Execute o arquivo `banco_oo_completo.py`:

```bash
python banco_oo_completo.py
```

3. Siga as opções do menu para criar clientes, contas e realizar operações.

## Estrutura das Classes

- **Cliente**: nome, CPF, senha, lista de contas
- **Conta**: número, cliente, saldo, histórico de transações
- **ContaCorrente**: herda de Conta, possui limite de saque
- **ContaPoupanca**: herda de Conta
- **Banco**: gerencia clientes, contas, autenticação e persistência

## Exemplo de uso do menu

```
=============== MENU BANCO ===============
[1] Novo cliente
[2] Nova conta
[3] Login cliente (operar conta)
[4] Listar clientes
[q] Sair
=>
```

## Expansões sugeridas

- Interface gráfica (Tkinter) ou web (Flask)
- Relatórios administrativos
- Testes unitários completos
- Integração com banco de dados

---

Desenvolvido por Sidnei Silva (sidneifs)
