# Estruturas de repetição WHILE

# Exemplo 1

numero_sorteado = 15

numero_escolhido = int(input("Informe um número entre 1 e 20: "))

while numero_escolhido != numero_sorteado:
    print("Você errou, tente novamente...")
    numero_escolhido = int(input("Informe um número entre 1 e 20: "))

print("Parabéns! Você acertou!")

# Exemplo 2
# Estruturas de repetição WHILE

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

print("Obrigado por usar nosso sistema bancário, até logo!")