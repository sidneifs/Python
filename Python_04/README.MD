# Variáveis e Constantes no Python

Este repositório contém o arquivo `variaveis_e_constantes.py`, que demonstra o uso de variáveis e constantes no Python de forma prática e simples.

---

## Variáveis

As variáveis são usadas para armazenar valores que podem ser alterados durante a execução do programa. No Python, o tipo da variável é inferido automaticamente com base no valor atribuído

### Exemplo

````python
age = 37
name = 'Sidnei'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

---
## Objetivos

Este exemplo simples demonstra como trabalhar com variáveis e constantes no Python. Apesar de o Python não ter suporte nativo para constantes, boas práticas como o uso de letras maiúsculas e tuplas ajudam a indicar valores que não devem ser alterados.

---

## Constantes

No Python, não há suporte nativo para constantes, mas por convenção utilizamos nomes em letras maiúsculas para indicar valores que não devem ser alterados.

### Exemplo:

```bash
PI = 3.14159265359
print(PI)
````

## Tuplas como Constantes

Tuplas são imutáveis, ou seja, seus valores não podem ser alterados após a criação. Elas são frequentemente usadas para representar constantes.

### Exemplo

BRASILIAN_STATES = ('MG', 'SP', 'RJ', 'ES')
print(BRASILIAN_STATES)

## Código Completo

Aqui está o código completo do arquivo variaveis_e_constantes.py:

```
age = 37
name = 'Sidnei'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

age, name = (37, 'Sidnei')
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

limite_saque_diario = 1000

stateS = 'MG'
stateS = 'SP' # Não é uma constante, pois pode ser alterada
BRASILIAN_STATES = ('MG', 'SP', 'RJ', 'ES') # Tupla é uma constante

PI = 3.14159265359
print(PI)
PI = 3.14 # Não é uma constante, pois pode ser alterada
print(PI)

print(BRASILIAN_STATES)
print(stateS)
print(limite_saque_diario)
```

## Executando o Código

Para executar o script, use o comando no terminal:

```bash
python variaveis_e_constantes.py
```

---

## O script exibirá os valores das variáveis, constantes e tuplas no terminal.

## Agradecimentos

Agradeço à DIO.me e à Suzano pela oportunidade de participar do Bootcamp Python Developer, que proporcionou o aprendizado e desenvolvimento deste projeto. ```

Sidnei Silva(sidnefs)
