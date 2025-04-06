# Estruturas Condicionais Aninhadas
# Estruturas condicionais aninhadas são estruturas condicionais dentro de outras estruturas condicionais.
# Elas são usadas quando precisamos verificar múltiplas condições de forma hierárquica.
# A sintaxe é a mesma das estruturas condicionais simples, mas com um nível adicional de indentação para cada nível de aninhamento.
# Exemplo de Estruturas Condicionais Aninhadas
# Vamos criar um sistema de saque bancário que verifica o tipo de conta do cliente e o saldo disponível.
# Dependendo do tipo de conta, o cliente pode sacar um valor diferente.
# O cliente pode ter uma conta normal, uma conta universitária ou uma conta especial.
# O cliente pode sacar até o saldo disponível, ou usar o cheque especial se o saldo for insuficiente.
# O cheque especial é um valor adicional que o banco disponibiliza para o cliente, mas que deve ser pago posteriormente.
# O cliente pode usar o cheque especial apenas se o saldo for insuficiente para o saque.
# Vamos criar um código que simula esse sistema de saque bancário.
# O código deve verificar o tipo de conta do cliente e o saldo disponível.
# Dependendo do tipo de conta, o cliente pode sacar um valor diferente.
# O cliente pode ter uma conta normal, uma conta universitária ou uma conta especial.
# O cliente pode sacar até o saldo disponível, ou usar o cheque especial se o saldo for insuficiente.
# O cheque especial é um valor adicional que o banco disponibiliza para o cliente, mas que deve ser pago posteriormente.
# O cliente pode usar o cheque especial apenas se o saldo for insuficiente para o saque.

# Estruturas Condicionais Aninhadas
# Simulação de um sistema de saque bancário que verifica o tipo de conta do cliente e o saldo disponível.

conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000  # Saldo disponível na conta
saque = 1500  # Valor que o cliente deseja sacar
cheque_especial = 450  # Valor do cheque especial disponível para o cliente

if conta_normal:  # Conta normal
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Saldo insuficiente para realizar o saque.")

elif conta_universitaria:  # Conta universitária
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente para realizar o saque.")

elif conta_especial:  # Conta especial
    print("Conta especial selecionada!")
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Saldo insuficiente para realizar o saque.")

else:  # Tipo de conta não reconhecido
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")