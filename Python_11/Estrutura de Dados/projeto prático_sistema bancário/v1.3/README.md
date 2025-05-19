# Sistema Bancário - SiD BANK

Bem-vindo ao **SiD BANK**, um sistema bancário simples e funcional desenvolvido em Python. Este projeto foi criado para gerenciar operações bancárias como depósitos, saques, geração de extratos, abertura de contas e funcionalidades administrativas.

---

## Funcionalidades Principais

- **Depósito**: Permite adicionar valores ao saldo da conta.
- **Saque**: Realiza saques com limite diário e por operação.
- **Extrato**: Gera um extrato detalhado das movimentações, incluindo um QR Code para acesso rápido.
- **Abertura de Conta Simples**: Cria uma nova conta com dados básicos e permite revisar os dados antes de salvar.
- **Listagem de Contas (Admin)**: Lista todas as contas cadastradas (acesso protegido por senha).
- **Testar Funcionalidades (Admin)**: Testa todas as funcionalidades do sistema (acesso protegido por senha).
- **Servidor Local**: Inicia um servidor local para exibir páginas HTML geradas, como o extrato.

---

## Atualizações Entre as Versões

### Versão 1.0

- Implementação inicial com funcionalidades básicas:
  - Depósito
  - Saque
  - Geração de extrato no terminal

### Versão 1.1

- Adicionada a funcionalidade de abertura de contas simples.
- Melhorias na organização do código.

### Versão 1.2

- Geração de extrato em arquivo `.txt`.
- Adicionado QR Code para acesso ao extrato.
- Implementação de um servidor local para exibir páginas HTML.

### Versão 1.3

- **Melhorias na Abertura de Conta**:
  - Adicionada a funcionalidade de revisar e atualizar os dados antes de salvar a conta.
  - Exibição dos dados inseridos para confirmação.
- **QR Code no HTML**:
  - O QR Code gerado é exibido diretamente na página HTML do extrato.
- **Funções Administrativas**:
  - Listagem de contas protegida por senha.
  - Teste de funcionalidades com geração de relatório.
- **Servidor Local**:
  - O servidor local é iniciado automaticamente para servir as páginas HTML geradas.

---

## Como Foi Realizada a Criação da Versão 1.3

A versão 1.3 trouxe melhorias significativas para o sistema bancário. Abaixo estão os detalhes das implementações realizadas:

### 1. **Melhorias na Abertura de Conta**

- Foi adicionada uma funcionalidade que permite ao usuário revisar os dados inseridos antes de salvar a conta.
- Exemplo:

  ```plaintext
  === Abertura de Conta Simples ===
  Informe o CPF ou CNPJ: 12345678900
  Informe o nome completo: João Silva
  Informe o CEP: 12345000
  Informe o logradouro: Rua das Flores
  Informe o número: 123
  Informe a cidade e sigla do estado (ex.: São Paulo-SP): São Paulo-SP
  Informe o complemento (opcional): Apartamento 101

  === Dados Inseridos ===
  CPF/CNPJ: 12345678900
  Nome: João Silva
  CEP: 12345000
  Logradouro: Rua das Flores
  Número: 123
  Cidade/Estado: São Paulo-SP
  Complemento: Apartamento 101

  Deseja atualizar os dados inseridos? (s/n): n
  === Conta criada com sucesso! Bem-vindo ao SiD BANK! ===

```


# Geração de QR Code no HTML

- O QR Code gerado para o extrato é exibido diretamente na página HTML.

## Exemplo de código HTML gerado:

```bash
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Extrato - SiD BANK</title>
</head>
<body>
    <h1>SiD BANK</h1>
    <h2>Extrato (Cliente)</h2>
    <p><strong>Protocolo:</strong> 20230518123045</p>
    <p><strong>Saldo:</strong> R$ 1500.00</p>
    <pre>Depósito: R$ 1500.00</pre>
    <p><strong>Link:</strong> <a href="www.sidbank.com/extrato/20230518123045" target="_blank">www.sidbank.com/extrato/20230518123045</a></p>
    <img src="extratos/extrato_20230518123045.png" alt="QR Code do Extrato">
</body>
</html>
```

# Menu do Sistema Bancário

- O menu principal foi mantido e atualizado para incluir todas as funcionalidades:

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

# Servidor Local

- Um servidor local é iniciado automaticamente para exibir as páginas HTML geradas, como o extrato.
- O servidor é acessado pelo navegador no endereço <http://localhost:8000>.

## Como Executar o Sistema

1. Certifique-se de que o Python 3 está instalado em sua máquina.
2. Clone este repositório ou baixe os arquivos.
3. No terminal, navegue até o diretório do projeto.
4. Execute o programa com o comando:

```bash
python projeto_sistema_bancario_v1.3.py
```

5. Siga as instruções no menu para realizar as operações desejadas.

# Estrutura do Projeto

```plaintext
projeto_sistema_bancario/
│
├── extratos/                # Diretório para salvar os extratos gerados
├── movimentacoes/           # Diretório para salvar movimentações (futuro)
├── testes/                  # Diretório para salvar relatórios de testes
├── projeto_sistema_bancario_v1.3.py  # Código principal do sistema
└── README.md                # Documentação do projeto
```

## Agradecimentos

Obrigado por utilizar o SiD BANK! Este projeto foi desenvolvido com o objetivo de aprendizado e prática em Python. Caso tenha sugestões ou melhorias, sinta-se à vontade para contribuir.

Sidnei Silva [(sidneifs)](https://github.com/sidneifs)
