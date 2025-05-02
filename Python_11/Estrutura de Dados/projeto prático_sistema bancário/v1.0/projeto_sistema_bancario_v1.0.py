import textwrap

def menu():
    menu = """\n
    =====================================
                SiD BANK
    =====================================
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [q]  Sair
    =====================================
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def main():
    LIMITE_SAQUES = 3
    LIMITE_SAQUE_VALOR = 500

    saldo = 0
    extrato = ""
    numero_saques = 0

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo, valor, extrato, LIMITE_SAQUE_VALOR, numero_saques, LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("\n=== Obrigado por usar o SiD BANK! Até logo! ===")
            break

        else:
            print("\n@@@ Operação inválida! Tente novamente. @@@")

main()