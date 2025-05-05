# Sistema Bancário em Python - SiD BANK (v1.2)

Este repositório contém a versão 1.2 do sistema bancário desenvolvido para o **SiD BANK**. Esta versão inclui melhorias como separação de funções administrativas, geração de QR Code com abertura no navegador, organização de dados em pastas específicas, melhorias no teste de funcionalidades e mensagens apropriadas para listagem de contas.

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
   - Gera um link e protocolo único para o extrato.
   - Cria um QR Code para acesso ao extrato.
   - Salva o extrato em um arquivo na pasta `extratos`.
   - Abre o link do extrato no navegador.

4. **Abrir Conta Simples**:
   - Permite criar uma conta fornecendo CPF/CNPJ, nome completo e endereço.
   - Cada conta é registrada com a data e hora de criação.

5. **Listar Contas (Admin)**:
   - Exibe todas as contas cadastradas.
   - Caso não haja contas registradas, exibe a mensagem: `"Não há registros de contas na data e hora atual: <data e hora atual>"`.
   - Requer autenticação com senha administrativa (`1234`).

6. **Testar Funcionalidades (Admin)**:
   - Permite testar todas as opções do menu.
   - Requer autenticação com senha administrativa (`1234`).
   - Salva os resultados do teste na pasta `testes`.

7. **Sair**:
   - Encerra o sistema com uma mensagem de despedida.

---

## Organização de Dados

- **Pasta `extratos`**: Contém os arquivos de extratos gerados.
- **Pasta `movimentacoes`**: Reservada para futuras implementações de movimentações detalhadas.
- **Pasta `testes`**: Contém os resultados dos testes realizados.

---

## Como Executar o Sistema

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a biblioteca `qrcode`:

   ```bash
   pip install qrcode[pil]
   ```

3. Navegue até o diretório onde o arquivo `projeto_sistema_bancario_v1.2.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python\Python_11\Estrutura de Dados\projeto prático_sistema bancário\v1.2"
   ```

4. Execute o arquivo diretamente no terminal:

   ```bash
   python projeto_sistema_bancario_v1.2.py
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
[cs] Abrir Conta Simples
[lc] Listar Contas (Admin)
[test] Testar Funcionalidades (Admin)
[q]  Sair
=====================================
=> 
```

### Exemplo de Listagem de Contas (Admin)

#### Sem contas registradas

```plaintext
Não há registros de contas na data e hora atual: 2025-05-05 14:30:00
```

#### Com contas registradas

```plaintext
=== Listagem de Contas ===

CPF/CNPJ: 12345678900
Nome: João Silva
Endereço: Rua das Flores, 123 - São Paulo-SP
Complemento: N/A
Data/Hora de Criação: 2025-05-05 14:00:00

CPF/CNPJ: 98765432100
Nome: Maria Oliveira
Endereço: Avenida Brasil, 456 - Rio de Janeiro-RJ
Complemento: Apartamento 101
Data/Hora de Criação: 2025-05-05 14:15:00
==========================================
```

---

## Agradecimento

Obrigado por explorar este repositório! Espero que este projeto ajude a entender como criar um sistema bancário funcional em Python. Se tiver dúvidas ou sugestões, entre em contato.

Sidnei Silva [(sidneifs)](https://github.com/sidneifs)
