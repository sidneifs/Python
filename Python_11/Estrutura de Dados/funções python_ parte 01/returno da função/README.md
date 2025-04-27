# Funções em Python: Retorno de Valores

Este repositório contém o arquivo `01_retorno_da_funcao.py`, que demonstra como criar funções em Python que retornam valores. O retorno de valores é uma das características mais importantes das funções, permitindo que elas processem dados e devolvam resultados para serem utilizados em outras partes do programa.

---

## O que são Funções com Retorno?

Funções com retorno são aquelas que utilizam a palavra-chave `return` para devolver um valor ou múltiplos valores ao chamador. Isso permite que o resultado da função seja armazenado em variáveis ou utilizado diretamente em expressões.

### Estrutura Básica

```python
def nome_da_funcao(parametros):
    # processamento
    return resultado
```

---

## Exemplos no Código

### 1. Função `calcular_total`

Esta função recebe uma lista de números e retorna a soma de todos os elementos.

#### Código

```python
def calcular_total(numeros):
    return sum(numeros)
```

#### Exemplo de Uso

```python
print(calcular_total([1, 2, 3, 4, 5]))  # Saída: 15
print(calcular_total([10, 20, 34]))     # Saída: 64
```

---

### 2. Função `retorna_antecessor_e_sucessor`

Esta função recebe um número inteiro e retorna o antecessor e o sucessor do número. Ela também realiza validações para garantir que o número seja um inteiro positivo e menor ou igual a 100.

#### Código

```python
def retorna_antecessor_e_sucessor(numero):
    if not isinstance(numero, int):
        raise ValueError("O número deve ser um inteiro.")
    if numero < 0:
        raise ValueError("O número deve ser positivo.")
    if numero > 100:
        raise ValueError("O número deve ser menor ou igual a 100.")
    
    antecessor = numero - 1
    sucessor = numero + 1

    if numero == 0:
        antecessor = -1
        sucessor = 1
    elif numero == 100:
        antecessor = 99
        sucessor = 101

    return antecessor, sucessor
```

#### Exemplo de Uso

```python
print(retorna_antecessor_e_sucessor(10))   # Saída: (9, 11)
print(retorna_antecessor_e_sucessor(0))    # Saída: (-1, 1)
print(retorna_antecessor_e_sucessor(100))  # Saída: (99, 101)
print(retorna_antecessor_e_sucessor(50))   # Saída: (49, 51)
```

---

## Como Executar o Arquivo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde o arquivo `01_retorno_da_funcao.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python\Python_11\Estrutura de Dados\funções python_ parte 01\returno da função"
   ```

3. Execute o arquivo diretamente no terminal:

   ```bash
   python 01_retorno_da_funcao.py
   ```

4. O terminal exibirá os resultados das funções chamadas no código.

---

## Agradecimento

Obrigado por explorar este repositório! Espero que os exemplos ajudem a entender melhor como criar funções com retorno em Python. Se tiver dúvidas ou sugestões, entre em contato.

Sidnei Silva [(sidneifs)](https://github.com/sidneifs)
