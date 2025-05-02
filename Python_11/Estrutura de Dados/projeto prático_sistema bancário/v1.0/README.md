# Sistema Bancário em Python - SiD BANK

Este repositório contém a versão 1.0 do sistema bancário desenvolvido para o **SiD BANK**. O sistema permite realizar operações básicas como depósito, saque e exibição de extrato. Este projeto foi desenvolvido em Python como parte de um desafio para modernizar as operações bancárias.

---

## Funcionalidades

1. **Depósito**:
   - Permite adicionar valores positivos ao saldo da conta.
   - O valor depositado é registrado no extrato.

2. **Saque**:
   - Permite realizar saques com as seguintes restrições:
     - Limite de R$ 500,00 por saque.
     - Máximo de 3 saques diários.
     - O saque só é permitido se houver saldo suficiente.
   - O valor sacado é registrado no extrato.

3. **Extrato**:
   - Lista todos os depósitos e saques realizados na conta.
   - Exibe o saldo atual no formato `R$ xxx.xx`.
   - Caso não haja movimentações, exibe a mensagem: `"Não foram realizadas movimentações."`.

4. **Sair**:
   - Encerra o sistema com uma mensagem de despedida.

---

## Como Executar o Sistema

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde o arquivo `projeto_sistema_bancario_v1.0.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python\Python_11\Estrutura de Dados\projeto prático_sistema bancário\v1.0"
   ```

3. Execute o arquivo diretamente no terminal:

   ```bash
   python projeto_sistema_bancario_v1.0.py
   ```

---

## Exemplo de Uso

### Menu Principal

```plaintext
=====================================
                SiD BANK
=====================================
[d]  Depositar
[s]  Sacar
[e]  Extrato
[q]  Sair
=====================================
=> 
```

### Depósito

```plaintext
Informe o valor do depósito: 1000

=== Depósito realizado com sucesso! ===
```

### Saque

```plaintext
Informe o valor do saque: 500

=== Saque realizado com sucesso! ===
```

### Extrato

#### Cenário com Movimentações

```plaintext
================ EXTRATO ================
Depósito:       R$ 1000.00
Saque:          R$ 500.00

Saldo:          R$ 500.00
==========================================
```

#### Cenário Sem Movimentações

```plaintext
================ EXTRATO ================
Não foram realizadas movimentações.

Saldo:          R$ 0.00
==========================================
```

---

## Tecnologias Utilizadas

- **Python 3.10+**
- Estruturas de controle e funções para modularização do código.
- Manipulação de strings para formatação de valores monetários.

---

## Agradecimento

Obrigado por explorar este repositório! Espero que este projeto ajude a entender como criar um sistema bancário funcional em Python. Se tiver dúvidas ou sugestões, entre em contato.

Sidnei Silva [(sidneifs)](https://github.com/sidneifs)
