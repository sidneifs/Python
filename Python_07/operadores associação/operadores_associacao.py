# Operadores de associação
# São usados para verificar se um valor ou variável está presente em uma sequência (string, lista, tupla, dicionário, etc.).
# Os operadores de associação são: in e not in.

# Exemplo 1: Verificando se um elemento está presente ou não em uma lista
frutas = ["limao", "uva", "laranja"]  # Lista de frutas
curso = "Curso de Python"  # String com o nome do curso

print("uva" in frutas)  # True
print("laranja" in frutas)  # True
print("limao" in frutas)  # True
print("banana" not in frutas)  # True
print("Python" in curso)  # True
print("Java" not in curso)  # True

# Exemplo 2: Verificando se um elemento está presente ou não em um conjunto
saques = {1500, 100, 500, 2000}  # Conjunto de saques

print(1500 in saques)  # True
print(100 in saques)  # True
print(500 not in saques)  # False
print(3000 not in saques)  # True
print("1500" not in saques)  # True (string "1500" não está no conjunto)

# Exemplo 3: Verificando se um elemento está presente ou não em um dicionário
dados = {"nome": "João", "idade": 30, "cidade": "São Paulo"}  # Dicionário de dados

print("nome" in dados)  # True (chave "nome" está no dicionário)
print("João" in dados.values())  # True (valor "João" está no dicionário)
print("estado" not in dados)  # True (chave "estado" não está no dicionário)