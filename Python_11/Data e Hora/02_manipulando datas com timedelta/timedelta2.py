from datetime import datetime, timedelta 
# Importando módulos necessários

#Exemplo de uso de timedelta
from datetime import date, datetime, timedelta

tipo_carro = "M"  # P, M, G # P = Pequeno, M = Médio, G = Grande
tempo_pequeno = 30 # dias
tempo_medio = 45 # dias
tempo_grande = 60 # dias
data_atual = datetime.now() # Obtendo a data atual

if tipo_carro == "P": # Se o carro for pequeno
    data_estimada = data_atual - timedelta(days=tempo_pequeno) # Exemplo de timedelta de 30 dias
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}") # Exibindo data estimada para carro pequeno
elif tipo_carro == "M": # Se o carro for médio
    data_estimada = data_atual - timedelta(days=tempo_medio) # Exemplo de timedelta de 45 dia
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}") # Exibindo data estimada para carro médio
else:
    data_estimada = data_atual - timedelta(days=tempo_grande) # Exemplo de timedelta de 60 dias
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}") # Exibindo data estimada para carro grande


print(date.today() - timedelta(days=1)) # Exibindo a data de ontem

resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1) # Exibindo resultado da subtração de 1 hora
print(resultado) # Exibindo resultado - resultado: 2023-07-25 09:19:20
print(resultado.time())  # Exibindo apenas a hora do resultado - resultado: 09:19:20

print(datetime.now().date())# Exibindo a data atual


# Criando um objeto timedelta de 5 dias
delta = timedelta(days=5) # Exemplo de timedelta de 5 dias
# Exibindo o objeto timedelta
print("Objeto timedelta:", delta)  # Exibindo o objeto timedelta - resultado: 5 days, 0:00:00
# Exibindo dias, segundos e microsegundos do objeto timedelta
print("Dias:", delta.days)  # Exibindo dias - resultado: 5
print("Segundos:", delta.seconds)  # Exibindo segundos - resultado: 0
print("Microsegundos:", delta.microseconds)  # Exibindo microsegundos - resultado: 0
# Exibindo total de segundos do objeto timedelta
print("Total de segundos:", delta.total_seconds())  # Exibindo total de segundos - resultado: 432000.0

# Criando um objeto datetime atual
agora = datetime.now()  # Exibindo data e hora atual
print("Data e hora atual:", agora)  # Exibindo data e hora atual - resultado: 2023-10-31 15:30:00 (ou a data e hora atual)
# Adicionando o objeto timedelta à data atual
nova_data = agora + delta  # Adicionando 5 dias à data atual
print("Nova data (5 dias depois):", nova_data)  # Exibindo nova data - resultado: 2023-11-05 15:30:00 (ou a data atual + 5 dias)
# Subtraindo o objeto timedelta da data atual
nova_data_subtraida = agora - delta  # Subtraindo 5 dias da data atual
print("Nova data (5 dias antes):", nova_data_subtraida)  # Exibindo nova data - resultado: 2023-10-26 15:30:00 (ou a data atual - 5 dias)

# Comparando datas com timedelta
print("Data atual é maior que nova data?", agora > nova_data)  # True ou False
# Verificando se a nova data é igual à data atual mais 5 dias
print("Nova data é igual à data atual + 5 dias?", nova_data == agora + delta)  # True ou False
# Verificando se a nova data é igual à data atual menos 5 dias
print("Nova data é igual à data atual - 5 dias?", nova_data_subtraida == agora - delta)  # True ou False
# Verificando se a nova data é maior que a data atual
print("Nova data é maior que a data atual?", nova_data > agora)  # True ou False
# Verificando se a nova data é menor que a data atual
print("Nova data é menor que a data atual?", nova_data < agora)  # True ou False
# Verificando se a nova data é maior ou igual à data atual
print("Nova data é maior ou igual à data atual?", nova_data >= agora)  # True ou False
# Verificando se a nova data é menor ou igual à data atual
print("Nova data é menor ou igual à data atual?", nova_data <= agora)  # True ou False
# Verificando se a nova data é diferente da data atual
print("Nova data é diferente da data atual?", nova_data != agora)  # True ou False
# Verificando se a nova data é igual à data atual
print("Nova data é igual à data atual?", nova_data == agora)  # True ou False
# Verificando se a nova data é igual à data atual menos 5 dias
print("Nova data é igual à data atual - 5 dias?", nova_data_subtraida == agora - delta)  # True ou False
# Verificando se a nova data é igual à data atual mais 5 dias
print("Nova data é igual à data atual + 5 dias?", nova_data == agora + delta)  # True ou False
# Verificando se a nova data é maior que a data atual mais 5 dias
print("Nova data é maior que a data atual + 5 dias?", nova_data > agora + delta)  # True ou False
# Verificando se a nova data é menor que a data atual menos 5 dias
print("Nova data é menor que a data atual - 5 dias?", nova_data_subtraida < agora - delta)  # True ou False
# Verificando se a nova data é maior ou igual à data atual mais 5 dias
print("Nova data é maior ou igual à data atual + 5 dias?", nova_data >= agora + delta)  # True ou False
# Verificando se a nova data é menor ou igual à data atual menos 5 dias
print("Nova data é menor ou igual à data atual - 5 dias?", nova_data_subtraida <= agora - delta)  # True ou False   
# Verificando se a nova data é diferente da data atual mais 5 dias
print("Nova data é diferente da data atual + 5 dias?", nova_data != agora + delta)  # True ou False
# Verificando se a nova data é diferente da data atual menos 5 dias
print("Nova data é diferente da data atual - 5 dias?", nova_data_subtraida != agora - delta)  # True ou False
# Verificando se a nova data é igual à data atual
print("Nova data é igual à data atual?", nova_data == agora)  # True ou False
# Verificando se a nova data é igual à data atual menos 5 dias
print("Nova data é igual à data atual - 5 dias?", nova_data_subtraida == agora - delta)  # True ou False
# Verificando se a nova data é igual à data atual mais 5 dias
print("Nova data é igual à data atual + 5 dias?", nova_data == agora + delta)  # True ou False
# Verificando se a nova data é maior que a data atual
