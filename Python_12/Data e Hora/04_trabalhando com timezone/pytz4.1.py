# -*- coding: utf-8 -*-

# exemplo de uso de timezone com datetime
from datetime import datetime # import datetime

import pytz # import pytz para trabalhar com timezones
# pip install pytz # instalar pytz se não estiver instalado
# pytz é uma biblioteca que permite trabalhar com timezones de forma fácil e eficiente

data = datetime.now(pytz.timezone("Europe/Oslo")) # obtendo a data e hora atual em um timezone específico
data2 = datetime.now(pytz.timezone("America/Sao_Paulo")) # obtendo a data e hora atual em outro timezone específico

print(data) # exibindo a data e hora atual no timezone Europe/Oslo
# exibindo a data e hora atual no timezone America/Sao_Paulo
print(data2) # exibindo a data e hora atual no timezone America/Sao_Paulo
# convertendo a data e hora do timezone Europe/Oslo para America/Sao_Paulo
data_convertida = data.astimezone(pytz.timezone("America/Sao_Paulo"))
print(data_convertida) # exibindo a data e hora convertida para o timezone America/Sao_Paulo 
# convertendo a data e hora do timezone America/Sao_Paulo para Europe/Oslo
data_convertida2 = data2.astimezone(pytz.timezone("Europe/Oslo"))
print(data_convertida2) # exibindo a data e hora convertida para o timezone Europe/Oslo
# verificando se a data e hora atual no timezone Europe/Oslo é maior que a data e hora atual no timezone America/Sao_Paulo  
print(data > data2) # exibindo se a data e hora atual no timezone Europe/Oslo é maior que a data e hora atual no timezone America/Sao_Paulo
# verificando se a data e hora atual no timezone America/Sao_Paulo é maior que a data e hora atual no timezone Europe/Oslo
print(data2 > data) # exibindo se a data e hora atual no timezone America/Sao_Paulo é maior que a data e hora atual no timezone Europe/Oslo

