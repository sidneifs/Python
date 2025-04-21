# Interpolação de Variáveis em Python

Este repositório contém o arquivo `string_2.py`, que demonstra diferentes métodos de interpolação de variáveis em Python. A interpolação de variáveis é uma técnica usada para inserir valores de variáveis em strings, facilitando a formatação e exibição de dados.

---

## O que é Interpolação de Variáveis?

A interpolação de variáveis permite combinar texto e valores de variáveis em uma única string. Python oferece várias abordagens para realizar essa tarefa, cada uma com suas vantagens e casos de uso.

---

## Métodos de Interpolação de Variáveis

### 1. **Concatenação Simples**

A concatenação usa o operador `+` para unir strings e valores convertidos para string.

```python
nome = "Sidnei"
idade = 37
print("Nome: " + nome + " Idade: " + str(idade))
```

**Saída:**

```plaintext
Nome: Sidnei Idade: 37
```

---

### 2. **Interpolação com `%`**

Este método usa placeholders (`%s`, `%d`, `%f`) para inserir valores na string.

```python
nome = "Sidnei"
idade = 37
print("Nome: %s Idade: %d" % (nome, idade))
```

**Saída:**

```plaintext
Nome: Sidnei Idade: 37
```

---

### 3. **Método `str.format()`**

O método `format()` substitui placeholders `{}` pelos valores fornecidos.

#### Exemplo Básico

```python
nome = "Sidnei"
idade = 37
print("Nome: {} Idade: {}".format(nome, idade))
```

**Saída:**

```plaintext
Nome: Sidnei Idade: 37
```

#### Exemplo com Posições

```python
print("Nome: {1} Idade: {0}".format(idade, nome))
```

**Saída:**

```plaintext
Nome: Sidnei Idade: 37
```

#### Exemplo com Nomes

```python
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
```

**Saída:**

```plaintext
Nome: Sidnei Idade: 37
```

#### Exemplo com Dicionários

```python
dados = {"nome": "Sidnei", "idade": 37}
print("Nome: {nome} Idade: {idade}".format(**dados))
```

**Saída:**

```plaintext
Nome: Sidnei Idade: 37
```

---

### 4. **F-Strings (Python 3.6+)**

As f-strings são a forma mais moderna e eficiente de interpolação. Elas permitem inserir variáveis diretamente dentro de uma string, usando o prefixo `f` antes das aspas.

#### Exemplo Básico

```python
nome = "Sidnei"
idade = 37
print(f"Nome: {nome} Idade: {idade}")
```

**Saída:**

```plaintext
Nome: Sidnei Idade: 37
```

#### Exemplo com Formatação

```python
saldo = 1000.50
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
```

**Saída:**

```plaintext
Nome: Sidnei Idade: 37 Saldo: 1000.50
```

---

## Como Rodar o Arquivo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde o arquivo `string_2.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python\Python_10\interpolação de variáveis"
   ```

3. Execute o arquivo diretamente no terminal para visualizar os resultados:

   ```bash
   python string_2.py
   ```

4. O terminal exibirá os resultados das diferentes abordagens de interpolação de variáveis.

---

## Agradecimento

Obrigado por explorar este repositório! Espero que os exemplos ajudem a entender melhor como usar interpolação de variáveis em Python. Se tiver dúvidas ou sugestões, entre em contato.

Sidnei Silva [(sidneifs)](https://github.com/sidneifs)
