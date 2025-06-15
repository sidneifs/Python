# Menu Bancário com POO em Python

Este exemplo mostra como implementar um menu bancário simples utilizando Programação Orientada a Objetos.

## O que é?

- Um menu interativo para operações bancárias básicas (depósito, saque, extrato, sair).
- Utiliza uma classe `Conta` para encapsular dados e métodos de uma conta bancária.

## Exemplo de uso

```python
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
```

## Funcionamento

- O usuário pode depositar, sacar, ver o extrato ou sair.
- O saldo é atualizado conforme as operações.
- O menu é exibido até o usuário escolher sair.

---

Execute o arquivo `poo_menu_bancario.py` para ver o exemplo na prática.
