# Classes Abstratas em Python

Este exemplo mostra como criar e usar classes abstratas em Python usando o módulo `abc`.

## O que são?

- **Classe abstrata:** Serve como base para outras classes. Não pode ser instanciada diretamente.
- **Método abstrato:** Método que deve ser implementado pelas subclasses.

## Exemplo de uso

```python
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

class Carro(Veiculo):
    def mover(self):
        print("O carro está andando.")

class Barco(Veiculo):
    def mover(self):
        print("O barco está navegando.")

if __name__ == "__main__":
    # v = Veiculo()  # Isso gera erro! Não pode instanciar classe abstrata
    c = Carro()
    c.mover()
    b = Barco()
    b.mover()
```

## Saída esperada

```
O carro está andando.
O barco está navegando.
```

- Tentar instanciar `Veiculo` gera erro.
- As subclasses implementam o método abstrato `mover`.

---

Execute o arquivo `poo_abstratas.py` para ver o exemplo na prática.
