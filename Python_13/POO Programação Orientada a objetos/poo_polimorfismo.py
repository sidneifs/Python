# Exemplo: Polimorfismo em Python

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

# Exemplo de uso
if __name__ == "__main__":
    formas = [Quadrado(4), Circulo(3)]
    for forma in formas:
        print(f"Área: {forma.area():.2f}")
