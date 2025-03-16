# Variáveis e Constantes no Python

Este repositório contém o arquivo `variaveis_e_constantes.py`, que demonstra o uso de variáveis e constantes no Python. Abaixo, explicamos de forma simplificada os conceitos abordados no código.

---

## Variáveis

As variáveis são usadas para armazenar valores que podem ser alterados durante a execução do programa. No Python, não é necessário declarar o tipo da variável, pois ele é inferido automaticamente com base no valor atribuído.

### Exemplos no código:

````python
age = 37
name = 'Sidnei'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

_age_ e _name_ são variáveis que armazenam, respectivamente, um número inteiro e uma string.
O valor de uma variável pode ser alterado:

stateS = 'MG'
stateS = 'SP'  # O valor foi alterado de 'MG' para 'SP'

Constantes
No Python, não há suporte nativo para constantes (valores que não podem ser alterados). No entanto, por convenção, utilizamos nomes em letras maiúsculas para indicar que uma variável deve ser tratada como constante.

Exemplos no código:

PI = 3.14159265359
print(PI)
PI = 3.14  # Apesar de ser tratado como constante, o valor pode ser alterado
print(PI)

PI é uma constante por convenção, mas o Python permite que seu valor seja alterado.

Tuplas como Constantes

Tuplas são imutáveis, o que significa que seus valores não podem ser alterados após a criação. Por isso, elas são frequentemente usadas para representar constantes.

Exemplo no código:

BRASILIAN_STATES = ('MG', 'SP', 'RJ', 'ES')
print(BRASILIAN_STATES)

BRASILIAN_STATES é uma tupla que contém os estados brasileiros e não pode ser modificada.

Código Completo
Aqui está o código completo do arquivo variaveis_e_constantes.py:

age = 37
name = 'Sidnei'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

age, name = (37, 'Sidnei')
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

limite_saque_diario = 1000

stateS = 'MG'
stateS = 'SP'   # Não é uma constante, pois pode ser alterada
BRASILIAN_STATES = ('MG', 'SP', 'RJ', 'ES')  # Tupla é uma constante

PI = 3.14159265359
print(PI)
PI = 3.14  # Não é uma constante, pois pode ser alterada
print(PI)

print(BRASILIAN_STATES)
print(stateS)
print(limite_saque_diario)

Observações

Variáveis: Use para valores que podem mudar durante a execução do programa.
Constantes: Use nomes em letras maiúsculas para indicar valores que não devem ser alterados, mesmo que o Python permita a modificação.
Tuplas: São úteis para representar conjuntos de valores imutáveis.

Executando o Código

Para executar o script variaveis_e_constantes.py, use o comando no terminal:

python [variaveis_e_constantes.py](http://_vscodecontentref_/0)

O script exibirá os valores das variáveis, constantes e tuplas no terminal.

```markdown
# Variáveis e Constantes no Python

Este repositório contém o arquivo `variaveis_e_constantes.py`, que demonstra o uso de variáveis e constantes no Python. Abaixo, explicamos de forma simplificada os conceitos abordados no código.

---

## Variáveis

As variáveis são usadas para armazenar valores que podem ser alterados durante a execução do programa. No Python, não é necessário declarar o tipo da variável, pois ele é inferido automaticamente com base no valor atribuído.

### Exemplos no código:
```python
age = 37
name = 'Sidnei'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')
```
- `age` e `name` são variáveis que armazenam, respectivamente, um número inteiro e uma string.
- O valor de uma variável pode ser alterado:
  ```python
  stateS = 'MG'
  stateS = 'SP'  # O valor foi alterado de 'MG' para 'SP'
  ```

---

## Constantes

No Python, não há suporte nativo para constantes (valores que não podem ser alterados). No entanto, por convenção, utilizamos nomes em letras maiúsculas para indicar que uma variável deve ser tratada como constante.

### Exemplos no código:
```python
PI = 3.14159265359
print(PI)
PI = 3.14  # Apesar de ser tratado como constante, o valor pode ser alterado
print(PI)
```
- `PI` é uma constante por convenção, mas o Python permite que seu valor seja alterado.

---

## Tuplas como Constantes

Tuplas são imutáveis, o que significa que seus valores não podem ser alterados após a criação. Por isso, elas são frequentemente usadas para representar constantes.

### Exemplo no código:
```python
BRASILIAN_STATES = ('MG', 'SP', 'RJ', 'ES')
print(BRASILIAN_STATES)
```
- `BRASILIAN_STATES` é uma tupla que contém os estados brasileiros e não pode ser modificada.

---

## Código Completo

Aqui está o código completo do arquivo `variaveis_e_constantes.py`:

```python
age = 37
name = 'Sidnei'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

age, name = (37, 'Sidnei')
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

limite_saque_diario = 1000

stateS = 'MG'
stateS = 'SP'   # Não é uma constante, pois pode ser alterada
BRASILIAN_STATES = ('MG', 'SP', 'RJ', 'ES')  # Tupla é uma constante

PI = 3.14159265359
print(PI)
PI = 3.14  # Não é uma constante, pois pode ser alterada
print(PI)

print(BRASILIAN_STATES)
print(stateS)
print(limite_saque_diario)
```

---

## Observações

- **Variáveis**: Use para valores que podem mudar durante a execução do programa.
- **Constantes**: Use nomes em letras maiúsculas para indicar valores que não devem ser alterados, mesmo que o Python permita a modificação.
- **Tuplas**: São úteis para representar conjuntos de valores imutáveis.

---

## Executando o Código

Para executar o script `variaveis_e_constantes.py`, use o comando no terminal:

```bash
python variaveis_e_constantes.py
```

O script exibirá os valores das variáveis, constantes e tuplas no terminal.

---

## Objetivos

Este exemplo simples demonstra como trabalhar com variáveis e constantes no Python. Apesar de o Python não ter suporte nativo para constantes, boas práticas como o uso de letras maiúsculas e tuplas ajudam a indicar valores que não devem ser alterados.
```
````
