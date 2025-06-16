"""
Sistema Bancário Orientado a Objetos - Completo
- Validação de dados (CPF, valores, duplicidade)
- Persistência em arquivo JSON
- Autenticação de clientes por senha
- Tipos de conta (ContaCorrente, ContaPoupanca)
- Histórico de transações
- Interface CLI aprimorada
- Estrutura para testes automatizados
"""
import json
import os
from getpass import getpass

# Utilitários

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def carregar_dados(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"clientes": [], "contas": []}

def salvar_dados(arquivo, dados):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

# Classes
class Cliente:
    """Representa um cliente do banco."""
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.contas = []
    def adicionar_conta(self, conta):
        self.contas.append(conta)
    def __str__(self):
        return f"Cliente: {self.nome} | CPF: {self.cpf} | Contas: {[c.numero for c in self.contas]}"

class Conta:
    """Classe base para contas bancárias."""
    def __init__(self, numero, cliente, saldo=0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.transacoes = []
    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido!")
            return
        self.saldo += valor
        self.transacoes.append(("Depósito", valor))
    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido!")
            return
        if valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            self.transacoes.append(("Saque", -valor))
    def extrato(self):
        print(f"Conta: {self.numero} | Titular: {self.cliente.nome} | Saldo: R$ {self.saldo:.2f}")
        for tipo, valor in self.transacoes:
            print(f"  {tipo}: R$ {valor:.2f}")

class ContaCorrente(Conta):
    """Conta corrente com limite de saque."""
    def __init__(self, numero, cliente, saldo=0, limite=500):
        super().__init__(numero, cliente, saldo)
        self.limite = limite
    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print("Limite de saque excedido!")
        else:
            super().sacar(valor)

class ContaPoupanca(Conta):
    """Conta poupança simples."""
    pass

# Banco (gerenciador)
class Banco:
    """Gerenciador do sistema bancário: clientes, contas, autenticação e persistência."""
    def __init__(self, arquivo_dados="banco_dados.json"):
        self.arquivo = arquivo_dados
        self.dados = carregar_dados(self.arquivo)
        self.clientes = []
        self.contas = []
        self._carregar_objetos()
    def _carregar_objetos(self):
        cpf2cliente = {}
        for c in self.dados["clientes"]:
            cliente = Cliente(c["nome"], c["cpf"], c["senha"])
            self.clientes.append(cliente)
            cpf2cliente[c["cpf"]] = cliente
        for c in self.dados["contas"]:
            if c["tipo"] == "corrente":
                conta = ContaCorrente(c["numero"], cpf2cliente[c["cpf"]], c["saldo"])
            else:
                conta = ContaPoupanca(c["numero"], cpf2cliente[c["cpf"]], c["saldo"])
            conta.transacoes = c.get("transacoes", [])
            self.contas.append(conta)
            cpf2cliente[c["cpf"]].adicionar_conta(conta)
    def _salvar(self):
        clientes = [{"nome": c.nome, "cpf": c.cpf, "senha": c.senha} for c in self.clientes]
        contas = []
        for conta in self.contas:
            tipo = "corrente" if isinstance(conta, ContaCorrente) else "poupanca"
            contas.append({"numero": conta.numero, "cpf": conta.cliente.cpf, "saldo": conta.saldo, "tipo": tipo, "transacoes": conta.transacoes})
        salvar_dados(self.arquivo, {"clientes": clientes, "contas": contas})
    def novo_cliente(self):
        nome = input("Nome: ")
        cpf = input("CPF (11 dígitos): ")
        if not validar_cpf(cpf):
            print("CPF inválido!")
            return
        if any(c.cpf == cpf for c in self.clientes):
            print("Cliente já cadastrado!")
            return
        senha = getpass("Senha: ")
        cliente = Cliente(nome, cpf, senha)
        self.clientes.append(cliente)
        self._salvar()
        print("Cliente criado!")
    def nova_conta(self):
        cpf = input("CPF do titular: ")
        cliente = next((c for c in self.clientes if c.cpf == cpf), None)
        if not cliente:
            print("Cliente não encontrado!")
            return
        tipo = input("Tipo de conta ([1] Corrente, [2] Poupança): ")
        numero = len(self.contas) + 1
        if tipo == "1":
            conta = ContaCorrente(numero, cliente)
        else:
            conta = ContaPoupanca(numero, cliente)
        self.contas.append(conta)
        cliente.adicionar_conta(conta)
        self._salvar()
        print(f"Conta {numero} criada!")
    def autenticar(self):
        cpf = input("CPF: ")
        senha = getpass("Senha: ")
        cliente = next((c for c in self.clientes if c.cpf == cpf and c.senha == senha), None)
        if not cliente:
            print("Acesso negado!")
            return None
        return cliente
    def operacoes_conta(self, cliente):
        if not cliente.contas:
            print("Nenhuma conta cadastrada!")
            return
        print("Contas disponíveis:")
        for c in cliente.contas:
            print(f"[{c.numero}] {type(c).__name__} - Saldo: R$ {c.saldo:.2f}")
        numero = int(input("Escolha o número da conta: "))
        conta = next((c for c in cliente.contas if c.numero == numero), None)
        if not conta:
            print("Conta não encontrada!")
            return
        while True:
            print("[d] Depositar | [s] Sacar | [e] Extrato | [h] Histórico | [q] Sair")
            op = input("=> ")
            if op == "d":
                valor = float(input("Valor do depósito: "))
                conta.depositar(valor)
                self._salvar()
            elif op == "s":
                valor = float(input("Valor do saque: "))
                conta.sacar(valor)
                self._salvar()
            elif op == "e":
                conta.extrato()
            elif op == "h":
                for t, v in conta.transacoes:
                    print(f"{t}: R$ {v:.2f}")
            elif op == "q":
                break
            else:
                print("Opção inválida!")
    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente)
    def salvar_e_sair(self):
        self._salvar()
        print("Dados salvos. Saindo...")

# Interface CLI

def menu(idioma="pt"):
    opcoes = {
        "pt": [
            "\n=============== MENU BANCO ===============",
            "[1] Novo cliente",
            "[2] Nova conta",
            "[3] Login cliente (operar conta)",
            "[4] Listar clientes",
            "[5] Relatórios",
            "[q] Sair"
        ],
        "en": [
            "\n=============== BANK MENU ===============",
            "[1] New client",
            "[2] New account",
            "[3] Client login (operate account)",
            "[4] List clients",
            "[5] Reports",
            "[q] Quit"
        ]
    }
    for linha in opcoes[idioma]:
        print(linha)
    return input("=> ")

if __name__ == "__main__":
    idioma = input("Selecione o idioma / Select language [pt/en]: ").strip().lower()
    if idioma not in ("pt", "en"): idioma = "pt"
    banco = Banco()
    while True:
        op = menu(idioma)
        if op == "1":
            banco.novo_cliente()
        elif op == "2":
            banco.nova_conta()
        elif op == "3":
            if (cliente := banco.autenticar()):
                banco.operacoes_conta(cliente)
        elif op == "4":
            banco.listar_clientes()
        elif op == "5":
            print("\n=== Relatório de Clientes ===")
            banco.listar_clientes()
            print("\n=== Relatório de Contas ===")
            for conta in banco.contas:
                print(f"Conta: {conta.numero} | Titular: {conta.cliente.nome} | Saldo: R$ {conta.saldo:.2f}")
                print("Histórico:")
                for t, v in conta.transacoes:
                    print(f"  {t}: R$ {v:.2f}")
        elif op == "q":
            banco.salvar_e_sair()
            break
        else:
            print("Opção inválida!" if idioma == "pt" else "Invalid option!")
