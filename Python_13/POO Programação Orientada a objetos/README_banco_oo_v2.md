# Sistema Bancário Orientado a Objetos (Versão 2)

Este projeto apresenta uma versão aprimorada do sistema bancário, utilizando classes para representar clientes e contas, seguindo boas práticas de POO e um modelo UML simplificado.

## Funcionalidades

- Cadastro de clientes (com nome e CPF)
- Criação de contas bancárias associadas a clientes
- Depósito, saque e extrato por conta
- Listagem de todos os clientes e suas contas
- Menu interativo no terminal

## Como executar

1. Certifique-se de ter Python 3 instalado.
2. Execute o arquivo `banco_oo_v2.py`:

```bash
python banco_oo_v2.py
```

3. Siga as opções do menu para criar clientes, contas e realizar operações.

## Estrutura das Classes

- **Cliente**: nome, CPF, lista de contas
- **Conta**: número, cliente, saldo, métodos de depósito, saque e extrato

## Exemplo de uso

```
=============== MENU ================
[nu]    Novo usuário
[nc]    Nova conta
[d]     Depositar
[s]     Sacar
[e]     Extrato
[lc]    Listar clientes
[q]     Sair
=>
```

## Expansões sugeridas

- Persistência dos dados em arquivo ou banco de dados
- Autenticação por senha
- Tipos de conta (corrente, poupança)
- Relatórios e operações administrativas

---

Desenvolvido por Sidnei Silva (sidneifs)
