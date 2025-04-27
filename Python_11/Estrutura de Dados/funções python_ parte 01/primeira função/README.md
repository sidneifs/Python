# Introdução às Funções em Python

Este repositório contém o arquivo `00_primeira_funcao.py`, que demonstra como criar e utilizar funções em Python. Funções são blocos de código reutilizáveis que ajudam a organizar e simplificar programas, tornando-os mais legíveis e eficientes.

---

## O que são Funções?

Funções são blocos de código que realizam uma tarefa específica. Elas podem ser chamadas várias vezes ao longo do programa, evitando a repetição de código. Em Python, as funções são definidas usando a palavra-chave `def`.

### Estrutura Básica de uma Função

```python
def nome_da_funcao(parametros):
    # corpo da função
    return resultado
```

---

## Exemplos no Código

### 1. Função Simples

Uma função que exibe uma mensagem fixa.

```python
def exibir_mensagem():
    print("Hello World!")  # Exibe a mensagem
```

**Chamada da Função:**

```python
exibir_mensagem()
```

**Saída:**

```plaintext
Hello World!
```

---

### 2. Função com Parâmetro

Uma função que recebe um parâmetro e exibe uma mensagem personalizada.

```python
def exibir_mensagem_2(nome):
    print(f"Welcome {nome}!")  # Exibe a mensagem com o nome do usuário
```

**Chamada da Função:**

```python
exibir_mensagem_2("Sidnei")
```

**Saída:**

```plaintext
Welcome Sidnei!
```

---

### 3. Função com Parâmetro Padrão

Uma função que utiliza um valor padrão caso nenhum argumento seja fornecido.

```python
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Welcome {nome}!")  # Exibe a mensagem com o nome ou o valor padrão
```

**Chamada da Função:**

```python
exibir_mensagem_3()  # Sem argumento
exibir_mensagem_3("Sidnei")  # Com argumento
```

**Saída:**

```plaintext
Welcome Anônimo!
Welcome Sidnei!
```

---

### 4. Função com Múltiplos Parâmetros

Uma função que recebe dois parâmetros e exibe uma mensagem personalizada.

```python
def exibir_mensagem_4(nome="Anônimo", idade=0):
    print(f"Welcome {nome}! You are {idade} years old.")  # Exibe nome e idade
```

**Chamada da Função:**

```python
exibir_mensagem_4("Sidnei", 37)
exibir_mensagem_4()  # Utiliza os valores padrão
```

**Saída:**

```plaintext
Welcome Sidnei! You are 37 years old.
Welcome Anônimo! You are 0 years old.
```

---

## Como Executar o Arquivo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde o arquivo `00_primeira_funcao.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python\Python_11\Estrutura de Dados"
   ```

3. Execute o arquivo diretamente no terminal:

   ```bash
   python 00_primeira_funcao.py
   ```

4. O terminal exibirá as mensagens geradas pelas funções chamadas no código.

---

## Agradecimento

Obrigado por explorar este repositório! Espero que os exemplos ajudem a entender melhor como criar e utilizar funções em Python. Se tiver dúvidas ou sugestões, entre em contato.

Sidnei Silva [(sidneifs)](https://github.com/sidneifs)
