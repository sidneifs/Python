def calcular_total(numeros): # soma de todos os números
    return sum(numeros) # soma de todos os números

def retorna_antecessor_e_sucessor(numero): # antecessor e sucessor de um número
    if not isinstance(numero, int): # verifica se o número é inteiro
        raise ValueError("O número deve ser um inteiro.")
    if numero < 0: # verifica se o número é negativo
        raise ValueError("O número deve ser positivo.") # se o número for negativo, gera um erro
    if numero > 100: # verifica se o número é maior que 100
        raise ValueError("O número deve ser menor ou igual a 100.") # se o número for maior que 100, gera um erro 
    antecessor = numero - 1 # antecessor do número
    if numero == 0: # se o número for 0, o antecessor é -1
        antecessor = -1
    elif numero == 100: # se o número for 100, o sucessor é 101
        sucessor = 101
    else: # se o número for diferente de 0 e 100, o sucessor é o número + 1
        sucessor = numero + 1
    if numero == 0: # se o número for 0, o sucessor é 1
        sucessor = 1
    elif numero == 100: # se o número for 100, o antecessor é 99
        antecessor = 99
    else: # se o número for diferente de 0 e 100, o antecessor é o número - 1
        antecessor = numero - 1
    if numero == 0: # se o número for 0, o antecessor é -1
        antecessor = -1
    elif numero == 100: # se o número for 100, o sucessor é 101
        sucessor = 101
    else: # se o número for diferente de 0 e 100, o sucessor é o número + 1
        sucessor = numero + 1 # antecessor do número
    if numero == 0: # se o número for 0, o sucessor é 1

        return antecessor, sucessor # retorna o antecessor e o sucessor do número

# Testes
print(calcular_total([1, 2, 3, 4, 5]))  # 15     
print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)
print(retorna_antecessor_e_sucessor(0))  # (-1, 1)
print(retorna_antecessor_e_sucessor(100))  # (99, 101)
print(retorna_antecessor_e_sucessor(50))  # (49, 51)