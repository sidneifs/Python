from datetime import datetime, date, time
# Exemplo de uso de strftime e strptime para formatação e conversão de datas
# Criando uma data específica
data_especifica = datetime(2023, 10, 31, 15, 30, 0)  # 31 de outubro de 2023, 15:30:00
# Exibindo a data específica
print("Data específica:", data_especifica)  # Exibindo data específica - resultado: 2023-10-31 15:30:00

# Formatando a data específica como string
data_formatada = data_especifica.strftime("%d/%m/%Y %H:%M:%S")  # Formato: dia/mês/ano hora:minuto:segundo
print("Data formatada:", data_formatada)  # Exibindo data formatada - resultado: 31/10/2023 15:30:00

# Convertendo a string formatada de volta para um objeto datetime
data_convertida = datetime.strptime(data_formatada, "%d/%m/%Y %H:%M:%S")  # Convertendo de volta para datetime
print("Data convertida:", data_convertida)  # Exibindo data convertida - resultado: 2023-10-31 15:30:00

# Verificando se a data convertida é igual à data original
print("Data convertida é igual à data original?", data_convertida == data_especifica)  # True

# Exibindo a data convertida formatada novamente
print("Data convertida formatada:", data_convertida.strftime("%d/%m/%Y %H:%M:%S"))  # Exibindo data convertida formatada - resultado: 31/10/2023 15:30:00

# Exibindo a data atual
data_atual = datetime.now()  # Obtendo a data e hora atual
print("Data atual:", data_atual)  # Exibindo data atual - resultado: 2023-10-31 15:30:00 (ou a data e hora atual)

# Formatando a data atual como string
data_atual_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S")  # Formato: dia/mês/ano hora:minuto:segundo
print("Data atual formatada:", data_atual_formatada)  # Exibindo data atual formatada - resultado: 31/10/2023 15:30:00 (ou a data e hora atual)
# Convertendo a string da data atual de volta para um objeto datetime
data_atual_convertida = datetime.strptime(data_atual_formatada, "%d/%m/%Y %H:%M:%S")  # Convertendo de volta para datetime
print("Data atual convertida:", data_atual_convertida)  # Exibindo data atual convertida - resultado: 2023-10-31 15:30:00 (ou a data e hora atual)
# Verificando se a data atual convertida é igual à data original
print("Data atual convertida é igual à data original?", data_atual_convertida == data_atual)  # True
# Exibindo a data atual convertida formatada novamente
print("Data atual convertida formatada:", data_atual_convertida.strftime("%d/%m/%Y %H:%M:%S"))  # Exibindo data atual convertida formatada - resultado: 31/10/2023 15:30:00 (ou a data e hora atual)
# Exibindo a data atual como objeto date
print("Data atual como objeto date:", data_atual.date())  # Exibindo data atual como objeto date - resultado: 2023-10-31
# Exibindo a hora atual como objeto time
print("Hora atual como objeto time:", data_atual.time())  # Exibindo hora atual como objeto time - resultado: 15:30:00 (ou a hora atual)
# Exibindo o dia da semana da data atual (0=segunda, 6=domingo)
print("Dia da semana da data atual:", data_atual.weekday())  # Exibindo dia da semana da data atual - resultado: 1 (terça-feira)
# Exibindo o dia da semana da data atual como string
dias_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
print("Dia da semana da data atual (string):", dias_da_semana[data_atual.weekday()])  # Exibindo dia da semana da data atual como string - resultado: Terça
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (DD-MM-YYYY):", data_atual.strftime("%d-%m-%Y"))  # Exibindo data atual formatada - resultado: 31-10-2023
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (YYYY/MM/DD):", data_atual.strftime("%Y/%m/%d"))  # Exibindo data atual formatada - resultado: 2023/10/31
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (MM-DD-YYYY):", data_atual.strftime("%m-%d-%Y"))  # Exibindo data atual formatada - resultado: 10-31-2023
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (YYYY-MM-DD):", data_atual.strftime("%Y-%m-%d"))  # Exibindo data atual formatada - resultado: 2023-10-31
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (DD/MM/YYYY):", data_atual.strftime("%d/%m/%Y"))  # Exibindo data atual formatada - resultado: 31/10/2023
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (DD-MM-YYYY HH:MM:SS):", data_atual.strftime("%d-%m-%Y %H:%M:%S"))  # Exibindo data atual formatada - resultado: 31-10-2023 15:30:00
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (YYYY-MM-DD HH:MM:SS):", data_atual.strftime("%Y-%m-%d %H:%M:%S"))  # Exibindo data atual formatada - resultado: 2023-10-31 15:30:00
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (MM/DD/YYYY HH:MM:SS):", data_atual.strftime("%m/%d/%Y %H:%M:%S"))  # Exibindo data atual formatada - resultado: 10/31/2023 15:30:00
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (MM-DD-YYYY HH:MM:SS):", data_atual.strftime("%m-%d-%Y %H:%M:%S"))  # Exibindo data atual formatada - resultado: 10-31-2023 15:30:00
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (YYYY/MM/DD HH:MM:SS):", data_atual.strftime("%Y/%m/%d %H:%M:%S"))  # Exibindo data atual formatada - resultado: 2023/10/31 15:30:00
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (DD/MM/YYYY HH:MM:SS):", data_atual.strftime("%d/%m/%Y %H:%M:%S"))  # Exibindo data atual formatada - resultado: 31/10/2023 15:30:00
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (DD-MM-YYYY HH:MM:SS):", data_atual.strftime("%d-%m-%Y %H:%M:%S"))  # Exibindo data atual formatada - resultado: 31-10-2023 15:30:00
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (YYYY-MM-DD HH:MM:SS):", data_atual.strftime("%Y-%m-%d %H:%M:%S"))  # Exibindo data atual formatada - resultado: 2023-10-31 15:30:00
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (MM/DD/YYYY HH:MM:SS):", data_atual.strftime("%m/%d/%Y %H:%M:%S"))  # Exibindo data atual formatada - resultado: 10/31/2023 15:30:00    
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (MM-DD-YYYY HH:MM:SS):", data_atual.strftime("%m-%d-%Y %H:%M:%S"))  # Exibindo data atual formatada - resultado: 10-31-2023 15:30:00
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (YYYY/MM/DD HH:MM:SS):", data_atual.strftime("%Y/%m/%d %H:%M:%S"))  # Exibindo data atual formatada - resultado: 2023/10/31 15:30:00
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (DD/MM/YYYY HH:MM:SS):", data_atual.strftime("%d/%m/%Y %H:%M:%S"))  # Exibindo data atual formatada - resultado: 31/10/2023 15:30:00
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (DD-MM-YYYY HH:MM:SS):", data_atual.strftime("%d-%m-%Y %H:%M:%S"))  # Exibindo data atual formatada - resultado: 31-10-2023 15:30:00
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (YYYY-MM-DD HH:MM:SS):", data_atual.strftime("%Y-%m-%d %H:%M:%S"))  # Exibindo data atual formatada - resultado: 2023-10-31 15:30:00
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (MM/DD/YYYY HH:MM:SS):", data_atual.strftime("%m/%d/%Y %H:%M:%S"))  # Exibindo data atual formatada - resultado: 10/31/2023 15:30:00
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (MM-DD-YYYY HH:MM:SS):", data_atual.strftime("%m-%d-%Y %H:%M:%S"))  # Exibindo data atual formatada - resultado: 10-31-2023 15:30:00
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (YYYY/MM/DD HH:MM:SS):", data_atual.strftime("%Y/%m/%d %H:%M:%S"))  # Exibindo data atual formatada - resultado: 2023/10/31 15:30:00
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (DD/MM/YYYY HH:MM:SS):", data_atual.strftime("%d/%m/%Y %H:%M:%S"))  # Exibindo data atual formatada - resultado: 31/10/2023 15:30:00
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (DD-MM-YYYY HH:MM:SS):", data_atual.strftime("%d-%m-%Y %H:%M:%S"))  # Exibindo data atual formatada - resultado: 31-10-2023 15:30:00
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (YYYY-MM-DD HH:MM:SS):", data_atual.strftime("%Y-%m-%d %H:%M:%S"))  # Exibindo data atual formatada - resultado: 2023-10-31 15:30:00

#exmplo de steptime
# Exemplo de uso de strftime e strptime para formatação e conversão de datas
# Criando uma data específica   
data_especifica = datetime(2023, 10, 31, 15, 30, 0)  # 31 de outubro de 2023, 15:30:00
# Exibindo a data específica
print("Data específica:", data_especifica)  # Exibindo data específica - resultado: 2023-10-31 15:30:00
# Formatando a data específica como string
data_formatada = data_especifica.strftime("%d/%m/%Y %H:%M:%S")  # Formato: dia/mês/ano hora:minuto:segundo
print("Data formatada:", data_formatada)  # Exibindo data formatada - resultado: 31/10/2023 15:30:00
# Convertendo a string formatada de volta para um objeto datetime
data_convertida = datetime.strptime(data_formatada, "%d/%m/%Y %H:%M:%S")  # Convertendo de volta para datetime
print("Data convertida:", data_convertida)  # Exibindo data convertida - resultado: 2023-10-31 15:30:00
# Verificando se a data convertida é igual à data original
print("Data convertida é igual à data original?", data_convertida == data_especifica)  # True
# Exibindo a data convertida formatada novamente
print("Data convertida formatada:", data_convertida.strftime("%d/%m/%Y %H:%M:%S"))  # Exibindo data convertida formatada - resultado: 31/10/2023 15:30:00
# Exibindo a data atual
data_atual = datetime.now()  # Obtendo a data e hora atual
print("Data atual:", data_atual)  # Exibindo data atual - resultado: 2023-10-31 15:30:00 (ou a data e hora atual)
# Formatando a data atual como string
data_atual_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S")  # Formato: dia/mês/ano hora:minuto:segundo
print("Data atual formatada:", data_atual_formatada)  # Exibindo data atual formatada - resultado: 31/10/2023 15:30:00 (ou a data e hora atual)
# Convertendo a string da data atual de volta para um objeto datetime
data_atual_convertida = datetime.strptime(data_atual_formatada, "%d/%m/%Y %H:%M:%S")  # Convertendo de volta para datetime 
print("Data atual convertida:", data_atual_convertida)  # Exibindo data atual convertida - resultado: 2023-10-31 15:30:00 (ou a data e hora atual)
# Verificando se a data atual convertida é igual à data original
print("Data atual convertida é igual à data original?", data_atual_convertida == data_atual)  # True
# Exibindo a data atual convertida formatada novamente
print("Data atual convertida formatada:", data_atual_convertida.strftime("%d/%m/%Y %H:%M:%S"))  # Exibindo data atual convertida formatada - resultado: 31/10/2023 15:30:00 (ou a data e hora atual)
# Exibindo a data atual como objeto date
print("Data atual como objeto date:", data_atual.date())  # Exibindo data atual como objeto date - resultado: 2023-10-31
# Exibindo a hora atual como objeto time
print("Hora atual como objeto time:", data_atual.time())  # Exibindo hora atual como objeto time - resultado: 15:30:00 (ou a hora atual)
# Exibindo o dia da semana da data atual (0=segunda, 6=domingo
print("Dia da semana da data atual:", data_atual.weekday())  # Exibindo dia da semana da data atual - resultado: 1 (terça-feira)
# Exibindo o dia da semana da data atual como string
dias_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
print("Dia da semana da data atual (string):", dias_da_semana[data_atual.weekday()])  # Exibindo dia da semana da data atual como string - resultado: Terça
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (DD-MM-YYYY):", data_atual.strftime("%d-%m-%Y"))  # Exibindo data atual formatada - resultado: 31-10-2023
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (YYYY/MM/DD):", data_atual.strftime("%Y/%m/%d"))  # Exibindo data atual formatada - resultado: 2023/10/31
# Exibindo a data atual formatada em um formato diferente
print("Data atual formatada (MM-DD-YYYY):", data_atual.strftime("%m-%d-%Y"))  # Exibindo data atual formatada - resultado: 10-31-2023
# Exibindo a data atual formatada em um formato diferente

#exemplo de strftime e strptime para formatação e conversão de datas
# from datetime import datetime

data_hora_atual = datetime.now() # Obtendo a data e hora atual
data_hora_str = "2023-10-20 10:20" # String de data e hora a ser convertida
# Definindo as máscaras de formatação
mascara_ptbr = "%d/%m/%Y %a" # Formato: dia/mês/ano dia_da_semana
mascara_en = "%Y-%m-%d %H:%M" 

print(data_hora_atual.strftime(mascara_ptbr)) # Exibindo a data e hora atual formatada em português

data_convertida = datetime.strptime(data_hora_str, mascara_en) # Convertendo a string de data e hora para um objeto datetime
data_convertida = data_convertida.strftime(mascara_ptbr) # Formatando a data convertida para o formato em português
print(data_convertida) # Exibindo a data convertida formatada em português
# Exibindo o tipo da data convertida
print(type(data_convertida)) # Resultado: <class 'str'>, pois a data foi convertida para string após a formatação
# Exibindo a data e hora atual formatada em inglês
print(data_hora_atual.strftime(mascara_en)) # Exibindo a data e hora atual formatada em inglês
# Exibindo o tipo da data e hora atual
print(type(data_hora_atual)) # Resultado: <class 'datetime.datetime'>, pois a data e hora atual é um objeto datetime
# Exibindo a data e hora atual formatada em português
print(data_hora_atual.strftime(mascara_ptbr))  # Exibindo a data e hora atual formatada em português - resultado: 31/10/2023 Terça
# Exibindo o tipo da data e hora atual formatada
print(type(data_hora_atual.strftime(mascara_ptbr)))  # Resultado: <class 'str'>, pois a data e hora atual formatada é uma string
# Exibindo a data e hora atual formatada em inglês
print(data_hora_atual.strftime(mascara_en))  # Exibindo a data e hora atual formatada em inglês - resultado: 2023-10-31 15:30:00
# Exibindo o tipo da data e hora atual formatada em inglês
print(type(data_hora_atual.strftime(mascara_en)))  # Resultado: <class 'str'>, pois a data e hora atual formatada em inglês é uma string
# Exibindo a data e hora atual formatada em português
print(data_hora_atual.strftime(mascara_ptbr))  # Exibindo a data e hora atual formatada em português - resultado: 31/10/2023 Terça

