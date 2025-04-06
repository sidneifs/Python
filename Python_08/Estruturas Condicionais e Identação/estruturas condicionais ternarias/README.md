# Estruturas Condicionais Ternárias

## Estruturas condicionais ternárias são uma forma compacta de escrever uma estrutura condicional simples

### Elas são usadas para atribuir um valor a uma variável com base em uma condição

### A sintaxe é

## variavel = valor_se_verdadeiro if condicao else valor_se_falso

## Simulação de um sistema de saque bancário que verifica o saldo disponível e o valor do saque

saldo = 200000  # Saldo disponível na conta
saque = 2500    # Valor do saque solicitado

## Usando uma estrutura condicional ternária para determinar o status do saque

status = "Sucesso" if saldo >= saque else "Falha"

## Exibindo mensagens com base no status

if saldo >= saque:
    print("Realizando saque!")  # Se o saldo for suficiente, o saque é realizado com sucesso.
else:
    print("Saque não realizado!")  # Caso contrário, o saque falha.

## Exibindo o status final do saque

print(f"{status} ao realizar o saque!")  # Mensagem indicando o status do saque.
