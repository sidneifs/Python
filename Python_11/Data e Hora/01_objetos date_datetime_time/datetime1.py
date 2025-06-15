# Exemplo de uso de date, datetime e time
# Importando módulos necessários
from datetime import datetime, timedelta, date, time

data = date(2023, 7, 10) # Criando um objeto date com ano, mês e dia
print(data) # Exibindo a data atual - resultado: 2023-07-10
print(date.today()) # Exibindo a data de hoje - resultado: 2023-07-10 (ou a data atual)

data_hora = datetime(2023, 7, 10) # Criando um objeto datetime com ano, mês e dia
print(data_hora) # Exibindo a data e hora atual - resultado: 2023-07-10 00:00:00
print(datetime.today()) # Exibindo a data e hora de hoje - resultado: 2023-07-10 00:00:00 (ou a data e hora atual

hora = time(10, 20, 0) # Criando um objeto time com hora, minuto e segundo
print(hora) # Exibindo a hora atual - resultado: 10:20:00

# Data e hora atual
agora = datetime.now() #reusltado: 2023-10-31 15:30:00 (ou a data e hora atual)
# Exibindo data e hora atual
print("Data e hora atual:", agora) # Exibindo data e hora atual - resultado: 2023-10-31 15:30:00 (ou a data e hora atual)
# Exibindo apenas a data
print("Data atual:", agora.date())
# Exibindo apenas a hora
print("Hora atual:", agora.time())
# Exibindo ano, mês e dia
print("Ano:", agora.year)
print("Mês:", agora.month)
print("Dia:", agora.day)
# Exibindo hora, minuto e segundo
print("Hora:", agora.hour)
print("Minuto:", agora.minute)
print("Segundo:", agora.second)

# Exibindo dia da semana (0=segunda, 6=domingo)
print("Dia da semana:", agora.weekday())  # 0=segunda, 6=domingo
# Exibindo dia da semana como string
dias_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
print("Dia da semana (string):", dias_da_semana[agora.weekday()])
# Exibindo data e hora formatada
print("Data e hora formatada:", agora.strftime("%d/%m/%Y %H:%M:%S"))

# Exibindo data e hora ISO 8601
print("Data e hora ISO 8601:", agora.isoformat())

# Exibindo timestamp (segundos desde 1/1/1970)
print("Timestamp:", agora.timestamp())

# Adicionando 5 dias à data atual
nova_data = agora + timedelta(days=5)
print("Nova data (5 dias depois):", nova_data)

# Subtraindo 3 horas da hora atual
nova_hora = agora - timedelta(hours=3)
print("Nova hora (3 horas antes):", nova_hora)

# Criando uma data específica
data_especifica = datetime(2023, 10, 31, 15, 30, 0) # 31 de outubro de 2023, 15:30:00
print("Data específica:", data_especifica) # Exibindo data específica

# Comparando datas
print("Data atual é maior que data específica?", agora > data_especifica)  # True ou False
# Verificando se duas datas são iguais
print("Data atual é igual a data específica?", agora.date() == data_especifica.date())  # True ou False 
# Verificando se uma data é anterior a outra
print("Data atual é anterior a data específica?", agora < data_especifica)  # True ou False
# Verificando se uma data é posterior a outra
print("Data atual é posterior a data específica?", agora > data_especifica)  # True ou False
# Verificando se uma data está dentro de um intervalo
data_inicio = datetime(2023, 10, 1) # 1 de outubro de 2023
data_fim = datetime(2023, 10, 31) # 31 de outubro de 2023
print("Data atual está entre 1/10/2023 e 31/10/2023?", data_inicio <= agora <= data_fim)  # True ou False
# Verificando se uma data é um feriado (exemplo simples)
feriados = [
    datetime(2023, 1, 1),  # Ano Novo
    datetime(2023, 12, 25),  # Natal
]
print("Data atual é um feriado?", agora.date() in [f.date() for f in feriados])  # True ou False
# Verificando se uma data é um fim de semana
print("Data atual é um fim de semana?", agora.weekday() >= 5)  # True se sábado ou domingo
# Verificando se uma data é um dia útil
print("Data atual é um dia útil?", agora.weekday() < 5)  # True se segunda a sexta
# Verificando se uma data é um dia de trabalho
print("Data atual é um dia de trabalho?", agora.weekday() < 5 and agora.hour >= 9 and agora.hour < 18)  # True se segunda a sexta, entre 9h e 18h
# Verificando se uma data é um dia de descanso
print("Data atual é um dia de descanso?", agora.weekday() >= 5 or (agora.weekday() == 4 and agora.hour >= 18))  # True se sábado, domingo ou sexta após 18h
# Verificando se uma data é um dia de férias
print("Data atual é um dia de férias?", agora.month == 12 and agora.day >= 20)  # Exemplo: férias de dezembro após o dia 20
# Verificando se uma data é um dia de trabalho remoto
print("Data atual é um dia de trabalho remoto?", agora.weekday() < 5 and (agora.month == 7 or agora.month == 8))  # Exemplo: trabalho remoto em julho e agosto
# Verificando se uma data é um dia de reunião
print("Data atual é um dia de reunião?", agora.weekday() == 2 and agora.hour >= 10 and agora.hour < 12)  # Exemplo: reuniões às quartas-feiras entre 10h e 12h
# Verificando se uma data é um dia de entrega de projeto
print("Data atual é um dia de entrega de projeto?", agora.month == 12 and agora.day == 31)  # Exemplo: entrega de projeto no último dia do ano
# Verificando se uma data é um dia de folga
print("Data atual é um dia de folga?", agora.weekday() == 5 or agora.weekday() == 6)  # True se sábado ou domingo
