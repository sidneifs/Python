# Exemplo: Classes Abstratas em Python
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

# Exemplo de uso
if __name__ == "__main__":
    # v = Veiculo()  # Isso gera erro! Não pode instanciar classe abstrata
    c = Carro()
    c.mover()
    b = Barco()
    b.mover()
