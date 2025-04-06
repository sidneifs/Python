# Estruturas Condicionais Ternárias
# Estruturas condicionais ternárias são uma forma compacta de escrever uma estrutura condicional simples.
# Elas são usadas quando precisamos atribuir um valor a uma variável com base em uma condição.
# A sintaxe é a seguinte:
# variavel = valor_se_verdadeiro if condicao else valor_se_falso
# Exemplo de Estruturas Condicionais Ternárias
# Vamos criar um sistema de saque bancário que verifica o saldo disponível e o valor do saque.
# Dependendo do saldo, o saque pode ser realizado ou não.
# O código deve verificar se o saldo é suficiente para realizar o saque.
# Se o saldo for suficiente, o saque é realizado com sucesso. Caso contrário, o saque falha.
# O código deve imprimir uma mensagem indicando o status do saque.
# O código deve usar uma estrutura condicional ternária para verificar o saldo e o saque.
# Estruturas Condicionais Ternárias
# Simulação de um sistema de saque bancário que verifica o saldo disponível e o valor do saque.

# Dependendo do saldo, o saque pode ser realizado ou não.
saldo = 200000  # Saldo disponível na conta
saque = 2500    # Valor do saque solicitado

# Usando uma estrutura condicional ternária para determinar o status do saque
status = "Sucesso" if saldo >= saque else "Falha"

# Exibindo mensagens com base no status
if saldo >= saque:
    print("Realizando saque!")  # Se o saldo for suficiente, o saque é realizado com sucesso.
else:
    print("Saque não realizado!")  # Caso contrário, o saque falha.

# Exibindo o status final do saque
print(f"{status} ao realizar o saque!")  # Mensagem indicando o status do saque.