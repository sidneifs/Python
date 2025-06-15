# Exemplo: Desafio Menu Bancário com POO

class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
    def extrato(self):
        print(f"Conta: {self.numero} | Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")

def menu():
    menu = """
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    => """
    return input(menu)

if __name__ == "__main__":
    conta = Conta(1, "Maria")
    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Valor do depósito: "))
            conta.depositar(valor)
        elif opcao == "s":
            valor = float(input("Valor do saque: "))
            conta.sacar(valor)
        elif opcao == "e":
            conta.extrato()
        elif opcao == "q":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
