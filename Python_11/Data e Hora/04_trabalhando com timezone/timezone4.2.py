## Exemplo de uso do timezone com datetime
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, timezone # Importando os módulos necessários

data_oslo = datetime.now(timezone(timedelta(hours=2))) # Obtendo a data e hora atual em Oslo (UTC+2)
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3))) # Obtendo a data e hora atual em São Paulo (UTC-3)
# Convertendo a data e hora de Oslo para São Paulo
data_convertida_oslo = data_oslo.astimezone(timezone(timedelta(hours=-3))) # Convertendo de Oslo para São Paulo
# Convertendo a data e hora de São Paulo para Oslo
data_convertida_sao_paulo = data_sao_paulo.astimezone(timezone(timedelta(hours=2))) # Convertendo de São Paulo para Oslo

# Exibindo as datas e horas
print(data_oslo) # Exibindo a data e hora atual em Oslo
print(data_sao_paulo) # Exibindo a data e hora atual em São Paulo

# Exibindo as datas convertidas
print(data_convertida_oslo) # Exibindo a data e hora convertida de Oslo para São Paulo
print(data_convertida_sao_paulo) # Exibindo a data e hora convertida de São Paulo para Oslo

# Comparando as datas e horas
print(data_oslo > data_sao_paulo) # Verificando se a data e hora de Oslo é maior que a de São Paulo
print(data_sao_paulo > data_oslo) # Verificando se a data e hora de São Paulo é maior que a de Oslo
# Verificando se as datas convertidas são iguais
print(data_convertida_oslo == data_convertida_sao_paulo) # Verificando se as datas convertidas são iguais
print(data_convertida_sao_paulo == data_convertida_oslo) # Verificando se as datas convertidas são iguais
# Verificando se a data e hora atual em Oslo é maior que a de São Paulo 
print(data_oslo > data_sao_paulo) # Verificando se a data e hora atual em Oslo é maior que a de São Paulo
# Verificando se a data e hora atual em São Paulo é maior que a de Oslo
print(data_sao_paulo > data_oslo) # Verificando se a data e hora atual em São Paulo é maior que a de Oslo
# Verificando se a data e hora atual em Oslo é igual à de São Paulo
print(data_oslo == data_sao_paulo) # Verificando se a data e hora atual em Oslo é igual à de São Paulo
# Verificando se a data e hora atual em São Paulo é igual à de Oslo
print(data_sao_paulo == data_oslo) # Verificando se a data e hora atual em São Paulo é igual à de Oslo
# Verificando se a data e hora atual em Oslo é maior que a data e hora convertida de São Paulo
print(data_oslo > data_convertida_sao_paulo) # Verificando se a data e hora atual em Oslo é maior que a convertida de São Paulo
# Verificando se a data e hora atual em São Paulo é maior que a data e hora convertida de Oslo
print(data_sao_paulo > data_convertida_oslo) # Verificando se a data e hora atual em São Paulo é maior que a convertida de Oslo
# Verificando se a data e hora convertida de Oslo é maior que a de São Paulo
print(data_convertida_oslo > data_convertida_sao_paulo) # Verificando se a data e hora convertida de Oslo é maior que a de São Paulo
# Verificando se a data e hora convertida de São Paulo é maior que a de Oslo
print(data_convertida_sao_paulo > data_convertida_oslo) # Verificando se a data e hora convertida de São Paulo é maior que a de Oslo
# Verificando se a data e hora atual em Oslo é igual à data e hora convertida de São Paulo
print(data_oslo == data_convertida_sao_paulo) # Verificando se a data e hora atual em Oslo é igual à convertida de São Paulo

