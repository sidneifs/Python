# Objetos date, datetime e time em Python

Este exemplo demonstra como criar e manipular objetos de data (`date`), data e hora (`datetime`) e hora (`time`) usando o módulo `datetime` do Python.

## Conceito

O módulo `datetime` permite trabalhar com datas e horários de forma simples e eficiente. Você pode criar datas específicas, obter a data/hora atual, acessar partes da data (ano, mês, dia, hora, minuto, segundo) e formatar a saída.

## Como utilizar

- Importe os objetos desejados: `from datetime import date, datetime, time`
- Crie datas e horários usando os construtores.
- Utilize métodos como `.today()`, `.now()`, `.strftime()` para manipulação e formatação.

## Exemplo

```python
from datetime import date, datetime, time
print(date.today())
print(datetime.now())
print(time(10, 20, 0))
```

Sidnei Silva (sidneifs)
