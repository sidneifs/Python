''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

import sys

try:
    # Lê a linha de entrada
    entrada = input().strip()

    # Tenta separar por ']' (formato padrão)
    if ']' in entrada:
        lista_str, limite_str = entrada.rsplit(']', 1)
    else:
        # Alternativa: separa por espaço
        lista_str, limite_str = entrada.split(' ', 1)
    lista_str = lista_str.replace('[', '').replace(']', '').replace(' ', '')
    transacoes = [float(x) for x in lista_str.split(',') if x]
    limite = float(limite_str.replace(',', '').strip())
    # Filtra as transações cujo valor absoluto é maior que o limite
    resultado = [int(x) if x == int(x) else x for x in transacoes if abs(x) > limite]
    print(f"Transações: {resultado}")
except Exception:
    print("Formato de entrada inválido. Use o formato: [n1,n2,n3], limite")
