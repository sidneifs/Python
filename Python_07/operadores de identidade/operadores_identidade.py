# Operadores de Identidade
# São utilizados para comparar objetos, verificando se são o mesmo objeto na memória.
# São eles: is e is not

# Exemplo 1: Verificando se duas variáveis são o mesmo objeto na memória
a = [1, 2, 3]   # Lista alocada na memória
b = a           # b aponta para o mesmo objeto que a na memória
c = [1, 2, 3]   # Outra lista alocada na memória
print(a is b)    # True, pois a e b apontam para o mesmo objeto na memória
print(a is c)    # False, pois a e c são objetos diferentes na memória
print(a is not b)  # False, pois a e b são o mesmo objeto na memória
print(a is not c)  # True, pois a e c são objetos diferentes na memória

# Exemplo 2: Verificando se uma variável é None
print(a is not None)  # True, pois a não é None
print(a is None)      # False, pois a não é None

# Caixa eletrônico
# Criando um caixa eletrônico simples
saldo = 10000  # Saldo inicial
saque = 2000   # Valor do saque
limite = 8000 # Limite de saque

# Verificando se o valor do saque é menor ou igual ao saldo
if saldo >= saque:
    print("Realizando saque")
    saldo -= saque  # Atualizando o saldo
    print(f"Novo saldo: {saldo}")
else:
    print("Saldo insuficiente")

# Verificando se o saldo é igual ao limite
if saldo == limite:
    print("Saldo igual ao limite")
else:
    print("Saldo diferente do limite")

# Verificando se o saldo é diferente do limite
if saldo != limite:
    print("Saldo diferente do limite")
else:
    print("Saldo igual ao limite")

# Verificando se o saldo e o limite são o mesmo objeto na memória
print(saldo is limite)       # False, pois saldo e limite são objetos diferentes
print(saldo is not limite)   # True, pois saldo e limite não são o mesmo objeto
print(saldo is not None)     # True, pois saldo não é None
print(saldo is None)         # False, pois saldo não é None
print(limite is not None)   # True, pois limite não é None
print(limite is None)       # False, pois limite não é None
print(saldo is not 10000)    # False, pois saldo é 10000
print(saldo is 10000)        # True, pois saldo é 10000
print(limite is not 8000)    # True, pois limite é 8000
print(limite is 8000)        # True, pois limite é 8000
print(saldo is not 8000)     # False, pois saldo é 10000
print(saldo is 8000)         # False, pois saldo é 10000
print(limite is not 10000)   # True, pois limite é 8000