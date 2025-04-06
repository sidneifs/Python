# Estruturas de Repetição: Loop FOR em Python

Este repositório contém o arquivo `estruturas_de_repeticao_FOR.py`, que demonstra o uso do loop `for` em Python. O loop `for` é uma das estruturas de repetição mais utilizadas e permite iterar sobre sequências ou iteráveis.

---

## O que é o Loop FOR?

O loop `for` é usado para percorrer elementos de uma sequência (como listas, strings, tuplas, dicionários ou conjuntos) ou iteráveis. Ele executa um bloco de código para cada elemento da sequência.

### Sintaxe

```python
for item in sequencia:
    # faça algo com o item
```

---

## Exemplos no Código

### Exemplo 1: Iterando sobre uma lista

O loop `for` percorre cada elemento de uma lista e executa um bloco de código para cada item.

```python
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)
```

### Exemplo 2: Iterando sobre um texto para encontrar vogais

O loop `for` pode ser usado para processar strings. No exemplo abaixo, o código verifica se cada letra do texto informado é uma vogal.

```python
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # Adiciona uma quebra de linha ao final
```

### Exemplo 3: Iterando com a função `range`

A função `range` é usada para gerar uma sequência de números. No exemplo abaixo, o loop `for` percorre números de 0 a 50, com um passo de 5.

```python
for numero in range(0, 51, 5):
    print(numero, end=" ")
```

---

## Como Rodar o Arquivo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório onde o arquivo `estruturas_de_repeticao_FOR.py` está localizado. No terminal, use o comando:

   ```bash
   cd "c:\Users\sucos\OneDrive\Documentos\PROJETOS Visual Studio CODE 2025\AULA 5 VS\Python\Python_09"
   ```

3. Execute o arquivo diretamente no terminal para visualizar os resultados:

   ```bash
   python estruturas_de_repeticao_FOR.py
   ```

4. O terminal exibirá os resultados das iterações realizadas no código.

---

## Exemplo de Saída

Dependendo da entrada do usuário e do código, você verá uma saída semelhante a esta:

```plaintext
maçã
banana
laranja
Informe um texto: Python
o
0 5 10 15 20 25 30 35 40 45 50
```

---

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou novos exemplos para o arquivo.

---

## Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).
