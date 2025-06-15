# Formatando e convertendo datas com strftime e strptime

Este exemplo ensina como formatar datas para string e converter strings para datas usando os métodos `strftime` e `strptime` do módulo `datetime`.

## Conceito

- `strftime` formata objetos de data/hora em strings com o padrão desejado.
- `strptime` converte strings formatadas em objetos de data/hora.

## Como utilizar

- Importe: `from datetime import datetime`
- Use `.strftime('%d/%m/%Y %H:%M:%S')` para formatar.
- Use `datetime.strptime(string, formato)` para converter.

## Exemplo

```python
from datetime import datetime
agora = datetime.now()
texto = agora.strftime('%d/%m/%Y %H:%M:%S')
print(texto)
data = datetime.strptime(texto, '%d/%m/%Y %H:%M:%S')
print(data)
```

Sidnei Silva (sidneifs)
