# Funções de Entrada e Saída no Python

Este repositório contém o arquivo `funcoes_entradas_saidas_input_builtin.py`, que demonstra o uso de funções de entrada e saída no Python, como `input()` e `print()`.

---

## Função `input()`

A função `input()` é usada para capturar dados fornecidos pelo usuário no terminal. O valor retornado por `input()` é sempre do tipo `str` (string).

### Exemplo

```python
nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

print(nome, idade)
```

» O programa solicita que o usuário insira o nome e a idade.

» Os valores digitados são armazenados nas variáveis `nome` e `idade`.

---

## Função `print()`

A função print() é usada para exibir informações no terminal. Ela possui parâmetros opcionais que permitem personalizar a saída.

Parâmetros do `print()`:

    1. sep: Define o separador entre os valores exibidos.

Padrão: espaço (`" "`).
Exemplo:

```python
print("Python", "é", "incrível", sep="-")
# Saída: Python-é-incrível
```

    2. end: Define o caractere ou string que será exibido ao final da linha.

Padrão: nova linha ("\n").
Exemplo:

```python
print("Olá", end="!!!\n")# Saída: Olá!!!
```

Exemplo no código:

```python
print(nome, idade)  # Exibe os valores separados por espaço
print(nome, idade, end="...\n")  # Adiciona "..." ao final da linha
print(nome, idade, sep="#", end="...\n")  # Usa "#" como separador e "..." no final
print(nome, idade, sep="#") # Usa "#" como separador
```

---

## Código Completo

Aqui está o código completo do arquivo `funcoes_entradas_saidas_input_builtin.py`:

```python
nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

print(nome, idade)
print(nome, idade, end="...\n")
print(nome, idade, sep="#", end="...\n")
print(nome, idade, sep="#")
```

---

## Executando o Código

Para executar o script, use o comando no terminal:

```bash
python 'funcoes_entradas_saidas_input_builtin.py'
```

Ver link do arquivo [aqui](https://github.com/sidneifs/Python/blob/main/Python_06/funcoes_entradas_saidas_input_builtin.py).

O programa solicitará que o usuário insira o nome e a idade e exibirá os resultados formatados no terminal.

---

## Agradecimentos

Agradeço à DIO.me e à Suzano pela oportunidade de participar do Bootcamp Python Developer, que proporcionou o aprendizado e desenvolvimento deste projeto.
