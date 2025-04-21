nome = "Sidnei" # string
idade = 37 # inteiro 
altura = 1.69 # float
e_maior = idade > 18 # booleano
peso = 80 # inteiro
profissao = "Progamador"
linguagem = "Python"
saldo = 1000.50 # float

print("Nome: " + nome + " Idade: " + str(idade)) # str() = converte para string
print("Nome: " + nome + " Idade: " + str(idade) + " Profissão: " + profissao + " Linguagem: " + linguagem)

dados = {"nome": "Sidnei", "idade": 28} # dicionário
print("Nome: " + dados["nome"] + " Idade: " + str(dados["idade"])) # dicionário

# Metodos de interpolação de variáveis

print("Nome: %s Idade: %d" % (nome, idade)) # %s = string, %d = inteiro, %f = float
print("Nome: %s Idade: %d" % (nome, idade)) # %s = string, %d = inteiro, %f = float

print("Nome: {} Idade: {}".format(nome, idade)) # {} = posição, {} = posição
print("Nome: {} Idade: {}".format(nome, idade)) # {} = posição, {} = posição

print("Nome: {1} Idade: {0}".format(idade, nome))   # {0} = posição, {1} = posição
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome)) # {0} = posição, {1} = posição

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade)) # {nome} = nome, {idade} = idade
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade)) # {nome} = nome, {idade} = idade
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome)) # {name} = nome, {age} = idade
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade)) # {nome} = nome, {idade} = idade
print("Nome: {nome} Idade: {idade}".format(**dados)) # {nome} = nome, {idade} = idade
print("Nome: {nome} Idade: {idade}".format(**dados)) # {nome} = nome, {idade} = idade

print(f"Nome: {nome} Idade: {idade}") # f"{}" = f-string
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")    # f"{}" = f-string
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")    # f"{}" = f-string
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo: 7.1f}")  # f"{}" = f-string