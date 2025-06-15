# Manipulando datas com timedelta em Python

Este exemplo mostra como usar o objeto `timedelta` do módulo `datetime` para realizar operações com datas e horários, como somar ou subtrair dias, horas e minutos.

## Conceito

O `timedelta` representa uma diferença entre duas datas ou horários. É útil para calcular prazos, datas futuras ou passadas e intervalos de tempo.

## Como utilizar

- Importe: `from datetime import datetime, timedelta`
- Some ou subtraia um `timedelta` de um objeto `date` ou `datetime`.

## Exemplo

```python
from datetime import datetime, timedelta
hoje = datetime.now()
ontem = hoje - timedelta(days=1)
print(ontem)
```

Sidnei Silva (sidneifs)
