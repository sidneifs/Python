# Estruturas condicionais e identação
# Identação e blocos de código em Python
# Identação é o espaço em branco no início de uma linha de código.
# Em Python, a identação é obrigatória e define o bloco de código que pertence a uma estrutura de controle (if, for, while, etc.).
# O bloco de código é o conjunto de instruções que serão executadas se a condição for verdadeira.
# A identação é feita com espaços ou tabulações, mas é recomendável usar espaços para manter a consistência.
# O padrão é usar 4 espaços para cada nível de identação.

# Exemplo:
if True: # Bloco if
    print("Bloco if") # Início do bloco if
def sacar(valor): # Definição da função sacar
    saldo = 500 # Saldo inicial

    if saldo >= valor: # Verifica se o saldo é maior ou igual ao valor a ser sacado
        print("valor sacado!") # Se sim, imprime mensagem de sucesso
        saldo -= valor # Atualiza o saldo
        print(f"Novo saldo: {saldo}") # Imprime o novo saldo
        depositar(valor) # Chama a função depositar
        print(f"Novo saldo: {saldo}") # Imprime o novo saldo após o depósito
    elif saldo == 0: # Verifica se o saldo é igual a zero
        print("saldo zerado!")
        print("retire o seu cartão.") # Imprime mensagem de erro    
    else: # Se não, executa o bloco else
        print("retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!") # Fim do bloco if
    return saldo # Retorna o saldo atualizado


def depositar(valor): # Definição da função depositar
    # Função para depositar um valor no saldo
    saldo = 500 # Saldo inicial
    if valor > 0: # Verifica se o valor a ser depositado é maior que zero
        print("Valor depositado!")
        print(f"Novo saldo: {saldo}") # Imprime o novo saldo
        saldo += valor # Atualiza o saldo
        print(f"Novo saldo: {saldo}") # Imprime o novo saldo após o depósito
        return saldo # Retorna o saldo atualizado
    saldo += valor # Atualiza o saldo
    print(f"Novo saldo: {saldo}") # Imprime o novo saldo após o depósito
    return saldo # Retorna o saldo atualizado
sacar(1000) # Chama a função sacar com o valor 1000
depositar(1000) # Chama a função depositar com o valor 1000
# Fim do código.
# O código acima é um exemplo de como usar identação e blocos de código em Python.