# Trabalhando com Timezone em Python

Este exemplo mostra como manipular datas e horários com fuso horário usando o módulo `datetime` e as bibliotecas `pytz` ou o próprio `timezone` do Python.

---

## Conceito

Timezone (fuso horário) é a informação de localização global associada a uma data/hora. O Python permite criar objetos datetime com timezone e converter entre diferentes fusos.

---

## Como utilizar

- Com `pytz`: `from datetime import datetime` e `import pytz`
- Com `timezone`: `from datetime import datetime, timezone, timedelta`
- Use `.astimezone()` para converter entre fusos.

---

## Exemplos práticos

### 1. Manipulando objetos date, datetime e time

```python
from datetime import date, datetime, time

# Data atual
print(date.today())
# Data e hora atual
print(datetime.now())
# Hora específica
print(time(10, 20, 0))
```

### 2. Operações com timedelta

```python
from datetime import datetime, timedelta

hoje = datetime.now()
cinco_dias_atras = hoje - timedelta(days=5)
print(cinco_dias_atras)
```

### 3. Formatando e convertendo datas (strftime e strptime)

```python
from datetime import datetime

agora = datetime.now()
texto = agora.strftime('%d/%m/%Y %H:%M:%S')
print(texto)
data = datetime.strptime(texto, '%d/%m/%Y %H:%M:%S')
print(data)
```

### 4. Trabalhando com timezone usando pytz

```python
from datetime import datetime
import pytz

agora_sp = datetime.now(pytz.timezone('America/Sao_Paulo'))
agora_oslo = datetime.now(pytz.timezone('Europe/Oslo'))
print(agora_sp)
print(agora_oslo)
# Convertendo entre fusos
print(agora_sp.astimezone(pytz.timezone('Europe/Oslo')))
```

### 5. Trabalhando com timezone usando o módulo padrão

```python
from datetime import datetime, timezone, timedelta

agora_sp = datetime.now(timezone(timedelta(hours=-3)))  # São Paulo (UTC-3)
agora_oslo = datetime.now(timezone(timedelta(hours=2)))  # Oslo (UTC+2)
print(agora_sp)
print(agora_oslo)
# Convertendo entre fusos
print(agora_sp.astimezone(timezone(timedelta(hours=2))))
```

---

Esses exemplos cobrem as principais operações com datas, horas, intervalos e fusos horários em Python.

Sidnei Silva (sidneifs)
