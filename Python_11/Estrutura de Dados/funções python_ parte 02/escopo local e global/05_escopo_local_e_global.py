#Escopoo local e global
# Escopo de variáveis em Python
# Variáveis globais e locais
# Variáveis globais são acessíveis em todo o programa
# Variáveis locais são acessíveis apenas dentro da função onde foram definidas

# Exemplo de variável global

salario = 2000  # Variável global


def salario_bonus(bonus): # Variável local
    global salario # Declara que a variável salario é global
    salario += bonus # Adiciona o bônus ao salário global
    return salario # Retorna o salário atualizado

# Exemplo de variável local
def salario_bonus_local(bonus): # Variável local
    salario = 2000  # Variável local
    salario += bonus # Adiciona o bônus ao salário local
    return salario # Retorna o salário atualizado

salario_bonus(500)  # 2500 # Chama a função e passa o valor do bônus
print(salario) # 2500 # Imprime o valor do salário global atualizado    