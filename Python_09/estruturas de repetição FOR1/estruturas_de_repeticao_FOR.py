# Estruturas de repetição FOR
# O loop for é utilizado para iterar sobre uma sequência (como uma lista, tupla, dicionário, conjunto ou string) ou um iterável (como um objeto que pode ser percorrido).

# A sintaxe básica do loop for é a seguinte:
# for item in sequencia:
#     # faça algo com o item
# O loop for executa um bloco de código para cada item na sequência ou iterável, permitindo que você processe cada elemento individualmente.
# O loop for é útil quando você sabe quantas iterações deseja fazer ou quando está lidando com uma sequência de elementos.
# Exemplo básico de uso do loop for

# Estruturas de repetição FOR
# O loop for é utilizado para iterar sobre uma sequência (como lista, tupla, dicionário, conjunto ou string) ou um iterável.

# A sintaxe básica do loop for é:
# for item in sequencia:
#     # faça algo com o item

# Exemplo 1: Iterando sobre uma lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

# Exemplo 2: Iterando sobre um texto para encontrar vogais
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # Adiciona uma quebra de linha ao final

# Exemplo 3: Iterando com a função range
# A função range é usada para gerar uma sequência de números.
for numero in range(0, 51, 5):  # Gera números de 0 a 50, com passo 5
    print(numero, end=" ")