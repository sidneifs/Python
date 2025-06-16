"""
Sistema Bancário Orientado a Objetos (Versão 2)
- Cliente e Conta como classes separadas
- Suporte a múltiplos clientes e contas
- Relacionamento Cliente <-> Conta
- Operações: criar cliente, criar conta, depositar, sacar, extrato
"""

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []
    def adicionar_conta(self, conta):
        self.contas.append(conta)
    def __str__(self):
        return f"Cliente: {self.nome} | CPF: {self.cpf} | Contas: {[c.numero for c in self.contas]}"

class Conta:
    def __init__(self, numero, cliente, saldo=0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
    def extrato(self):
        print(f"Conta: {self.numero} | Titular: {self.cliente.nome} | Saldo: R$ {self.saldo:.2f}")

clientes = []
contas = []

def menu():
    menu = """
    ================ MENU ================
    [nu]\tNovo usuário
    [nc]\tNova conta
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [lc]\tListar clientes
    [q]\tSair
    => """
    return input(menu)

def criar_cliente():
    nome = input("Nome do cliente: ")
    cpf = input("CPF: ")
    cliente = Cliente(nome, cpf)
    clientes.append(cliente)
    print(f"Cliente {nome} criado!")

def criar_conta():
    cpf = input("CPF do titular: ")
    cliente = next((c for c in clientes if c.cpf == cpf), None)
    if not cliente:
        print("Cliente não encontrado!")
        return
    numero = len(contas) + 1
    conta = Conta(numero, cliente)
    contas.append(conta)
    cliente.adicionar_conta(conta)
    print(f"Conta {numero} criada para {cliente.nome}!")

def depositar():
    numero = int(input("Número da conta: "))
    conta = next((c for c in contas if c.numero == numero), None)
    if not conta:
        print("Conta não encontrada!")
        return
    valor = float(input("Valor do depósito: "))
    conta.depositar(valor)
    print("Depósito realizado!")

def sacar():
    numero = int(input("Número da conta: "))
    conta = next((c for c in contas if c.numero == numero), None)
    if not conta:
        print("Conta não encontrada!")
        return
    valor = float(input("Valor do saque: "))
    conta.sacar(valor)

def extrato():
    numero = int(input("Número da conta: "))
    conta = next((c for c in contas if c.numero == numero), None)
    if not conta:
        print("Conta não encontrada!")
        return
    conta.extrato()

def listar_clientes():
    for cliente in clientes:
        print(cliente)

if __name__ == "__main__":
    while True:
        opcao = menu()
        if opcao == "nu":
            criar_cliente()
        elif opcao == "nc":
            criar_conta()
        elif opcao == "d":
            depositar()
        elif opcao == "s":
            sacar()
        elif opcao == "e":
            extrato()
        elif opcao == "lc":
            listar_clientes()
        elif opcao == "q":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
