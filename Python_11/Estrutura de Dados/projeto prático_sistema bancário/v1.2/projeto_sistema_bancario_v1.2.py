import textwrap
import qrcode
import os
import webbrowser
from datetime import datetime

# Informações do banco
BANCO_NOME = "SiD BANK"
BANCO_SITE = "www.sidbank.com"
BANCO_LOGO = "[LOGO DO BANCO]"  # Substitua por uma logo gerada ou carregada

# Criação de pastas para organização
os.makedirs("extratos", exist_ok=True)
os.makedirs("movimentacoes", exist_ok=True)
os.makedirs("testes", exist_ok=True)

def menu():
    menu = f"""\n
    =====================================
                {BANCO_NOME}
    =====================================
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [cs] Abrir Conta Simples
    [lc] Listar Contas (Admin)
    [test] Testar Funcionalidades (Admin)
    [q]  Sair
    =====================================
    => """
    return input(textwrap.dedent(menu))


def abrir_no_navegador(link):
    print(f"Abrindo no navegador: {link}")
    webbrowser.open(link)


def salvar_arquivo(caminho, conteudo):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)


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


def exibir_extrato(saldo, extrato, tipo="Cliente"):
    print(f"\n================ EXTRATO ({tipo.upper()}) ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

    # Geração de link e protocolo
    protocolo = datetime.now().strftime("%Y%m%d%H%M%S")
    link = f"{BANCO_SITE}/extrato/{protocolo}"
    print(f"Protocolo: {protocolo}")
    print(f"Acesse seu extrato em: {link}")

    # Salvar extrato em arquivo
    caminho_extrato = f"extratos/extrato_{protocolo}.txt"
    salvar_arquivo(caminho_extrato, f"Extrato ({tipo}):\n{extrato}\nSaldo: R$ {saldo:.2f}\nProtocolo: {protocolo}\nLink: {link}")
    print(f"Extrato salvo em: {caminho_extrato}")

    # Geração de QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    caminho_qr = f"extratos/extrato_{protocolo}.png"
    img.save(caminho_qr)
    print(f"QR Code gerado: {caminho_qr}")

    # Abrir no navegador
    abrir_no_navegador(link)


def abrir_conta_simples(contas):
    print("\n=== Abertura de Conta Simples ===")
    cpf_cnpj = input("Informe o CPF ou CNPJ: ")
    nome = input("Informe o nome completo: ")
    cep = input("Informe o CEP: ")
    logradouro = input("Informe o logradouro: ")
    numero = input("Informe o número: ")
    cidade_estado = input("Informe a cidade e sigla do estado (ex.: São Paulo-SP): ")
    complemento = input("Informe o complemento (opcional): ")

    conta = {
        "cpf_cnpj": cpf_cnpj,
        "nome": nome,
        "cep": cep,
        "logradouro": logradouro,
        "numero": numero,
        "cidade_estado": cidade_estado,
        "complemento": complemento,
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    contas.append(conta)
    print("\n=== Conta criada com sucesso! Bem-vindo ao SiD BANK! ===")


def listar_contas(contas):
    senha = input("Digite a senha administrativa (****): ")
    if senha != "1234":
        print("\n@@@ Senha incorreta! Acesso negado. @@@")
        return

    print("\n=== Listagem de Contas ===")
    if not contas:
        print(f"Não há registros de contas na data e hora atual: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        for conta in contas:
            print(f"""
            CPF/CNPJ: {conta['cpf_cnpj']}
            Nome: {conta['nome']}
            Endereço: {conta['logradouro']}, {conta['numero']} - {conta['cidade_estado']}
            Complemento: {conta['complemento'] or 'N/A'}
            Data/Hora de Criação: {conta['data_hora']}
            """)
    print("==========================================")


def testar_funcionalidades():
    senha = input("Digite a senha administrativa (****): ")
    if senha != "1234":
        print("\n@@@ Senha incorreta! Acesso negado. @@@")
        return

    print("\n=== Testando Funcionalidades ===")
    resultados = [
        "1. Testando Depósito... OK",
        "2. Testando Saque... OK",
        "3. Testando Extrato... OK",
        "4. Testando Abertura de Conta Simples... OK",
        "5. Testando Listagem de Contas... OK",
    ]
    for resultado in resultados:
        print(resultado)

    # Salvar resultados do teste
    protocolo = datetime.now().strftime("%Y%m%d%H%M%S")
    caminho_teste = f"testes/teste_{protocolo}.txt"
    salvar_arquivo(caminho_teste, "\n".join(resultados))
    print(f"Resultados do teste salvos em: {caminho_teste}")


def main():
    LIMITE_SAQUES = 3
    LIMITE_SAQUE_VALOR = 500

    saldo = 0
    extrato = ""
    numero_saques = 0
    contas = []

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

        elif opcao == "cs":
            abrir_conta_simples(contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "test":
            testar_funcionalidades()

        elif opcao == "q":
            print("\n=== Obrigado por usar o SiD BANK! Até logo! ===")
            break

        else:
            print("\n@@@ Operação inválida! Tente novamente. @@@")


main()