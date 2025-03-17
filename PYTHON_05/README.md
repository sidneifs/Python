# Convertendo Tipos de Variáveis e Operadores Aritméticos no Python

Este repositório contém o arquivo `convertendo_tipos_de_variaveis.py`, que demonstra como realizar conversões de tipos de variáveis e exemplos de operadores aritméticos no Python.

---

## Conversão de Tipos

No Python, é possível converter valores entre diferentes tipos de dados, como `int`, `float`, `str`, entre outros.

### Exemplos:

```python
print(int(5.568896))  # Converte um float para inteiro
print(float(5))       # Converte um inteiro para float
print(int("25"))      # Converte uma string para inteiro
print(float("25.16")) # Converte uma string para float
print(str(10))        # Converte um inteiro para string
```

Verificando o Tipo:

```python
valor = 10
valor_str = str(valor)
print(type(valor))      # <class 'int'>
print(type(valor_str))  # <class 'str'>
```

---

# Operadores Aritméticos

Os operadores aritméticos são usados para realizar cálculos matemáticos no Python.

Exemplos:

```python
print(10 + 10)  # Soma
print(10 - 10)  # Subtração
print(10 * 10)  # Multiplicação
print(10 / 10)  # Divisão (retorna float)
print(100 // 3) # Divisão inteira
print(100 % 3)  # Resto da divisão
print(100 ** 3) # Potência
print(100 ** 0.5) # Raiz quadrada
```

# Precedência de Operadores:

O Python segue a ordem de precedência matemática (parênteses, exponenciação, multiplicação/divisão, soma/subtração).

Exemplos:

```python
print(100 // 2 + 3)  # 50 + 3 = 53
print(100 / 2 * 3)   # 50.0 * 3 = 150.0
print(100 // 2 ** 3) # 50 // 8 = 6
print(100 / 2 ** 3 + 3) # 6.25 + 3 = 9.25
```

# Código Completo

Aqui está o código completo do arquivo

````bash
convertendo_tipos_de_variaveis.py```:

```python
print(int(5.568896))  # Converte um float para inteiro
print(float(5))       # Converte um inteiro para float
print(int("25"))      # Converte uma string para inteiro
print(float("25"))    # Converte uma string para float
print(float("25.16")) # Converte uma string para float
print(str(10))        # Converte um inteiro para string

valor = 10
valor_str = str(valor)
print(type(valor))      # <class 'int'>
print(type(valor_str))  # <class 'str'>

print(100 / 2)  # 50.0 (divisão retorna float)
print(100 // 2) # 50 (divisão inteira retorna int)
````

---

# Operadores aritméticos

```python
print(10 + 10)  # Soma
print(10 - 10)  # Subtração
print(10 * 10)  # Multiplicação
print(10 / 10)  # Divisão
print(100 / 3)
print(100 // 3)
print(100 % 3)  # Resto da divisão
print(100 ** 3) # Potência
print(100 ** 0.5) # Raiz quadrada
print(100 // 2 + 3)  # 50 + 3 = 53
print(100 / 2 + 3)   # 50.0 + 3 = 53.0
print(100 // 2 * 3)  # 50 * 3 = 150
print(100 / 2 * 3)   # 50.0 * 3 = 150.0
print(100 // 2 - 3)  # 50 - 3 = 47
print(100 / 2 - 3)   # 50.0 - 3 = 47.0
print(100 // 2 % 3)  # 50 % 3 = 2
print(100 / 2 % 3)   # 50.0 % 3 = 2.0
print(100 // 2 ** 3) # 50 // 8 = 6
print(100 / 2 ** 3)  # 50.0 / 8 = 6.25
print(100 // 2 ** 3 + 3) # 6 + 3 = 9
print(100 / 2 ** 3 + 3)  # 6.25 + 3 = 9.25
print(100 // 2 ** 3 * 3) # 6 * 3 = 18
print(100 / 2 ** 3 * 3)  # 6.25 * 3 = 18.75
print(100 // 2 ** 3 - 3) # 6 - 3 = 3
print(100 / 2 ** 3 - 3)  # 6.25 - 3 = 3.25
print(100 // 2 ** 3 % 3) # 6 % 3 = 0
```

Para esse contexto considerar apenas os exemplos de conversões de tipos de variáveis nas linahs iniciais.
_*Demais Operadores aritiméticos são referências e objetos de práticas.*_

---

# Executando o Código

Para executar o script, use o comando no terminal:
python [convertendo_tipos_de_variaveis.py](http://_vscodecontentref_/0)

O script exibirá os resultados das conversões e operações no terminal.

# Agradecimentos

Agradeço à DIO.me e à Suzano pela oportunidade de participar do Bootcamp Python Developer, que proporcionou o aprendizado e desenvolvimento deste projeto. ```
