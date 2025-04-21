# Fatiamento e Manipulação de Strings em Python

Este repositório contém o arquivo `string_3.py`, que demonstra como utilizar métodos de **fatiamento** e **manipulação de strings** em Python. Strings são uma das estruturas mais utilizadas em Python, e o fatiamento permite acessar partes específicas de uma string de forma eficiente.

---

## O que é Fatiamento de Strings?

O **fatiamento** é uma técnica que permite acessar partes de uma string usando índices. Em Python, as strings são indexadas, o que significa que cada caractere possui uma posição (índice), começando do zero.

### Sintaxe Básica

```python
string[inicio:fim:passo]
```

- **`inicio`**: Índice inicial (inclusivo).
- **`fim`**: Índice final (exclusivo).
- **`passo`**: Define o intervalo entre os índices.

---

## Exemplos de Fatiamento

### 1. Acessando Partes da String

```python
nome = "Sidnei Ferreira da Silva"
print(nome[0:6])  # Do índice 0 ao 5: 'Sidnei'
print(nome[7:15])  # Do índice 7 ao 14: 'Ferreira'
print(nome[:6])  # Do início ao índice 5: 'Sidnei'
print(nome[7:])  # Do índice 7 ao final: 'Ferreira da Silva'
```

### 2. Pulando Caracteres com o Passo

```python
print(nome[0:15:2])  # Do índice 0 ao 14, pulando de 2 em 2: 'Sdn er'
print(nome[::-1])  # String invertida: 'avliS ad arierreF iedniS'
print(nome[::-2])  # String invertida, pulando de 2 em 2: 'aiSadrer ieni'
```

### 3. Acessando Caracteres Específicos

```python
print(nome[0])  # Primeiro caractere: 'S'
print(nome[-1])  # Último caractere: 'a'
print(nome[-2])  # Penúltimo caractere: 'v'
```

---

## Métodos de Manipulação de Strings

### 1. Contagem de Caracteres

```python
print(nome.count('e'))  # Quantidade de 'e': 4
print(nome.count(' '))  # Quantidade de espaços: 3
```

### 2. Localizando Caracteres

```python
print(nome.find('e'))  # Índice do primeiro 'e': 3
print(nome.find('x'))  # Retorna -1 se o caractere não for encontrado
```

### 3. Substituindo Caracteres

```python
print(nome.replace('F', 'f'))  # Substitui 'F' por 'f': 'Sidnei ferreira da Silva'
print(nome.replace('a', '@'))  # Substitui 'a' por '@': 'Sidnei Ferreira d@ Silv@'
```

### 4. Alterando o Caso

```python
print(nome.upper())  # Tudo em maiúsculas: 'SIDNEI FERREIRA DA SILVA'
print(nome.lower())  # Tudo em minúsculas: 'sidnei ferreira da silva'
print(nome.title())  # Primeira letra de cada palavra em maiúscula: 'Sidnei Ferreira Da Silva'
print(nome.capitalize())  # Primeira letra da string em maiúscula: 'Sidnei ferreira da silva'
```

### 5. Removendo Espaços

```python
texto = "  Sidnei Silva  "
print(texto.strip())  # Remove espaços no início e no final: 'Sidnei Silva'
print(texto.lstrip())  # Remove espaços no início: 'Sidnei Silva  '
print(texto.rstrip())  # Remove espaços no final: '  Sidnei Silva'
```

### 6. Dividindo Strings

```python
print(nome.split())  # Divide a string em palavras: ['Sidnei', 'Ferreira', 'da', 'Silva']
print(nome.split('e'))  # Divide a string pelo caractere 'e': ['Sidn', 'i F', 'rr', 'ira da Silva']
```

---

## Como Rodar o Arquivo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde o arquivo `string_3.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python\Python_10\fatiamento de strings"
   ```

3. Execute o arquivo diretamente no terminal para visualizar os resultados:

   ```bash
   python string_3.py
   ```

4. O terminal exibirá os resultados das operações realizadas no código.

---

## Agradecimento

Obrigado por explorar este repositório! Espero que os exemplos ajudem a entender melhor como utilizar fatiamento e manipulação de strings em Python. Se tiver dúvidas ou sugestões, entre em contato.

Sidnei Silva [(sidneifs)](https://github.com/sidneifs)
