# Polimorfismo em Python

Este exemplo demonstra o conceito de polimorfismo em POO, permitindo que diferentes classes implementem métodos com o mesmo nome, mas comportamentos distintos.

## O que é Polimorfismo?

Polimorfismo é a capacidade de diferentes classes responderem ao mesmo método de formas diferentes. Isso permite escrever código mais flexível e reutilizável.

## Exemplo de uso

```python
class Forma:
    def area(self):
        raise NotImplementedError("Implemente o método area!")

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        import math
        return math.pi * self.raio ** 2

if __name__ == "__main__":
    formas = [Quadrado(4), Circulo(3)]
    for forma in formas:
        print(f"Área: {forma.area():.2f}")
```

## Saída esperada

```
Área: 16.00
Área: 28.27
```

- Cada classe filha implementa o método `area` de forma diferente.
- O laço percorre objetos de diferentes tipos, mas todos respondem ao método `area`.

---

Execute o arquivo `poo_polimorfismo.py` para ver o exemplo na prática.
