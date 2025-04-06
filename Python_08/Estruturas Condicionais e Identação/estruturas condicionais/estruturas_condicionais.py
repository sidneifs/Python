# Estruturas condicionais e Identação
# Estruturas condicionais são fundamentais na programação, pois permitem que o programa tome decisões com base em condições específicas.
# Estruturas condicionais são utilizadas para tomar decisões em um programa.
# Elas permitem que o programa execute diferentes blocos de código com base em condições específicas.
# As estruturas condicionais mais comuns em Python são: if, elif e else.
# A estrutura if é usada para verificar uma condição. Se a condição for verdadeira, o bloco de código dentro do if será executado.
# A estrutura elif (else if) é usada para verificar múltiplas condições. Se a condição do if for falsa, o programa verifica a condição do elif.
# A estrutura else é usada para executar um bloco de código quando todas as condições anteriores (if e elif) forem falsas.
# A estrutura if, elif e else pode ser aninhada, ou seja, você pode ter uma estrutura if dentro de outra estrutura if.
# Isso permite criar condições mais complexas e tomar decisões mais específicas.

# Exemplo de uso de estruturas condicionais em Python:
# Verificando se um número é par ou ímpar
# O operador % (módulo) é usado para verificar o resto da divisão de um número por 2.
# Se o resto for 0, o número é par; caso contrário, é ímpar.
# Exemplo de código:

MAIOR_IDADE = 18    # Definindo a maioridade como 18 anos
IDADE_ESPECIAL = 17 # Definindo uma idade especial como 17 anos

idade = int(input("Informe sua idade: ")) # Solicita ao usuário que informe sua idade
# A função int() converte a entrada do usuário (que é uma string) em um número inteiro.

if idade >= MAIOR_IDADE: # Verifica se a idade é maior ou igual à maioridade
    print("Maior de idade, pode tirar a CHN.") # Se a condição for verdadeira, imprime a mensagem correspondente
    # O bloco de código dentro do if só será executado se a condição for verdadeira.
else: # Caso contrário, executa o bloco de código dentro do else
    print("Ainda não pode tirar a CNH.") # Imprime a mensagem correspondente

if idade < MAIOR_IDADE:  # Verifica se a idade é menor que a maioridade
    print("Ainda não pode tirar a CNH.") # Se a condição for verdadeira, imprime a mensagem correspondente

if idade >= MAIOR_IDADE:  # Verifica se a idade é maior ou igual à maioridade
    print("Maior de idade, pode tirar a CHN.")  # Se a condição for verdadeira, imprime a mensagem correspondente
elif idade == IDADE_ESPECIAL:  # Verifica se a idade é igual à idade especial
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")  # Se a condição for verdadeira, imprime a mensagem correspondente
else:
    print("Ainda não pode tirar a CNH.")   # Se a condição for verdadeira, imprime a mensagem correspondente