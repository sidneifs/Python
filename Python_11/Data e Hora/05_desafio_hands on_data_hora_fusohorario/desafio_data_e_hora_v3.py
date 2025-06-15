"""
DESCRIÇÃO
Neste desafio, você terá a oportunidade de otimizar o Sistema Bancário previamente desenvolvido com o uso de funções Python. O objetivo é aprimorar a estrutura e a eficiência do sistema, implementando as operações de depósito, saque e extrato em funções específicas. Você terá a chance de refatorar o código existente, dividindo-o em funções reutilizáveis, facilitando a manutenção e o entendimento do sistema como um todo. Prepare-se para aplicar conceitos avançados de programação e demonstrar sua habilidade em criar soluções mais elegantes e eficientes utilizando Python.

Aprimoramentos da v3:
- Todas as operações principais (depósito, saque, extrato, criação de cliente e conta) estão em funções separadas e reutilizáveis.
- Validação de dados de entrada.
- Estrutura modular e fácil de expandir.
- Código mais limpo e didático.
"""

import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

# Classes Cliente e PessoaFisica para correção de erro NameError
class Cliente:
    def __init__(self, endereco, senha=None):
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0
        self.senha = senha or "1234"  # senha padrão para simulação

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco, senha=None):
        super().__init__(endereco, senha)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0.0
        self.transacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append(("Depósito", valor, datetime.now()))

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
            return False
        self.saldo -= valor
        self.transacoes.append(("Saque", -valor, datetime.now()))
        return True

    def extrato(self):
        print(f"\nExtrato da conta {self.numero} - Cliente: {self.cliente.nome}")
        if not self.transacoes:
            print("Nenhuma movimentação registrada.")
        else:
            for tipo, valor, data in self.transacoes:
                print(f"{data.strftime('%d/%m/%Y %H:%M:%S')} - {tipo}: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}\n")

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor):
        if self.saques_realizados >= self.limite_saques:
            print("Limite de saques diários atingido!")
            return False
        if valor > self.limite:
            print(f"O valor máximo para saque é R$ {self.limite:.2f}")
            return False
        if super().sacar(valor):
            self.saques_realizados += 1
            return True
        return False

def menu():
    menu = """
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas do usuário
    [nu]\tNovo usuário
    [rs]\tRecuperar senha
    [a]\tAcesso ADMIN
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def menu_admin():
    menu = """
    ================ MENU ADMIN ================
    [1]\tListar todos os clientes
    [2]\tListar todas as contas
    [q]\tSair do modo ADMIN
    => """
    return input(textwrap.dedent(menu))

# Funções aprimoradas para validação e entrada de dados

def input_float(msg):
    while True:
        try:
            valor = float(input(msg))
            if valor < 0:
                print("Valor não pode ser negativo!")
                continue
            return valor
        except ValueError:
            print("Valor inválido! Digite um número.")

def input_cpf(msg):
    cpf = input(msg).strip()
    if not cpf.isdigit() or len(cpf) != 11:
        print("CPF deve conter 11 dígitos numéricos.")
        return None
    return cpf

def solicitar_cpf():
    while True:
        cpf = input_cpf("Informe o CPF do cliente (apenas números, 11 dígitos): ")
        if cpf:
            return cpf

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

# Exemplo de função criar_cliente adaptada:
def criar_cliente(clientes):
    cpf = solicitar_cpf()
    if filtrar_cliente(cpf, clientes):
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    senha = input("Defina uma senha para o cliente: ")
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco, senha=senha)
    clientes.append(cliente)
    print("\n=== Cliente criado com sucesso! ===")

def criar_conta(numero_conta, clientes, contas):
    cpf = solicitar_cpf()
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    print("Tipos de conta disponíveis:")
    print("[1] Conta Corrente (limite de saque e limite diário)")
    print("[2] Conta Simples")
    tipo = input("Escolha o tipo de conta (1 ou 2): ")
    if tipo == "1":
        conta = ContaCorrente(numero_conta, cliente)
    else:
        conta = Conta(numero_conta, cliente)
    contas.append(conta)
    print(f"Conta {numero_conta} criada para o cliente {cliente.nome}.")
    # Permite múltiplas contas por cliente
    if hasattr(cliente, 'contas'):
        cliente.contas.append(conta)
    else:
        cliente.contas = [conta]

def depositar(clientes, contas=None):
    cpf = solicitar_cpf()
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    conta = buscar_conta_cliente(cliente, contas)
    if not conta:
        print("\n@@@ Conta não encontrada! @@@")
        return
    valor = input_float("Informe o valor do depósito: ")
    conta.depositar(valor)
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

def sacar(clientes, contas=None):
    cpf = solicitar_cpf()
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    conta = buscar_conta_cliente(cliente, contas)
    if not conta:
        print("\n@@@ Conta não encontrada! @@@")
        return
    valor = input_float("Informe o valor do saque: ")
    if conta.sacar(valor):
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

def exibir_extrato(clientes, contas=None):
    cpf = solicitar_cpf()
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    conta = buscar_conta_cliente(cliente, contas)
    if not conta:
        print("\n@@@ Conta não encontrada! @@@")
        return
    conta.extrato()

def buscar_conta_cliente(cliente, contas):
    contas_cliente = [conta for conta in contas if conta.cliente == cliente]
    if not contas_cliente:
        print("Nenhuma conta encontrada para este cliente.")
        return None
    if len(contas_cliente) == 1:
        return contas_cliente[0]
    print("Contas encontradas para o cliente:")
    for idx, conta in enumerate(contas_cliente, 1):
        print(f"[{idx}] Conta: {conta.numero} | Saldo: R$ {conta.saldo:.2f}")
    while True:
        try:
            escolha = int(input("Selecione o número da conta desejada: "))
            if 1 <= escolha <= len(contas_cliente):
                return contas_cliente[escolha - 1]
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite um número válido.")

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        print(f"Conta: {conta.numero} | Cliente: {conta.cliente.nome} | Saldo: R$ {conta.saldo:.2f}")
        if hasattr(conta.cliente, 'contas'):
            print(f"Contas do cliente: {[c.numero for c in conta.cliente.contas]}")

def autenticar_cliente(clientes):
    cpf = solicitar_cpf()
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return None
    senha = input("Digite sua senha: ")
    if senha != cliente.senha:
        print("Senha incorreta!")
        return None
    print(f"Bem-vindo, {cliente.nome}!")
    return cliente

def recuperar_senha(clientes):
    cpf = solicitar_cpf()
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    nova_senha = input("Digite a nova senha: ")
    cliente.senha = nova_senha
    print("Senha redefinida com sucesso!")

ADMIN_CPF = "00000000000"
ADMIN_SENHA = "admin123"

def autenticar_admin():
    print("Acesso restrito - ADMINISTRADOR")
    cpf = input("CPF do admin: ").strip()
    senha = input("Senha do admin: ").strip()
    if cpf == ADMIN_CPF and senha == ADMIN_SENHA:
        print("Acesso de administrador concedido!")
        return True
    print("Acesso negado!")
    return False

def listar_todos_clientes(clientes, admin_autenticado=False):
    if not admin_autenticado and not autenticar_admin():
        return
    print("\n=== Lista de todos os clientes cadastrados ===")
    for cliente in clientes:
        print(f"Nome: {cliente.nome} | CPF: {cliente.cpf} | Endereço: {cliente.endereco}")
    print("---------------------------------------------")

def listar_todas_contas(contas, admin_autenticado=False):
    if not admin_autenticado and not autenticar_admin():
        return
    print("\n=== Lista de todas as contas do sistema ===")
    for conta in contas:
        print(f"Conta: {conta.numero} | Cliente: {conta.cliente.nome} | Saldo: R$ {conta.saldo:.2f}")
    print("---------------------------------------------")

def main():
    clientes = []
    contas = []
    while True:
        opcao = menu()
        if opcao == "d":
            depositar(clientes, contas)
        elif opcao == "s":
            sacar(clientes, contas)
        elif opcao == "e":
            exibir_extrato(clientes, contas)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "rs":
            recuperar_senha(clientes)
        elif opcao == "a":
            if autenticar_admin():
                while True:
                    admin_opcao = menu_admin()
                    if admin_opcao == "1":
                        listar_todos_clientes(clientes, admin_autenticado=True)
                    elif admin_opcao == "2":
                        listar_todas_contas(contas, admin_autenticado=True)
                    elif admin_opcao == "q":
                        print("Saindo do modo ADMIN...")
                        break
                    else:
                        print("\n@@@ Opção inválida no menu ADMIN. @@@")
        elif opcao == "q":
            break
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

if __name__ == "__main__":
    main()