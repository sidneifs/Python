''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

import sys

def calcular_saldo(transacoes):
    saldo = 0

    # TODO: Itere sobre cada transação na lista:
    
        # TODO: Adicione o valor da transação ao saldo
        

    # TODO: Retorne o saldo formatado em moeda brasileira com duas casas decimais:
    

# Lê a linha de entrada, remove espaços e colchetes, e separa os valores por vírgula
entrada = sys.stdin.readline().strip()
entrada = entrada.replace('[', '').replace(']', '').replace(' ', '')
if entrada == '':
    transacoes = []
else:
    transacoes = [float(x) for x in entrada.split(',') if x]

saldo = sum(transacoes)
print(f"Saldo: R$ {saldo:.2f}")
