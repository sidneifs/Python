# Exemplo: Herança em Python

class Animal:
    def __init__(self, nome):
        self.nome = nome
    def falar(self):
        print(f"{self.nome} faz um som.")

class Cachorro(Animal):
    def falar(self):
        print(f"{self.nome} diz: Au Au!")

class Gato(Animal):
    def falar(self):
        print(f"{self.nome} diz: Miau!")

# Exemplo de uso
if __name__ == "__main__":
    a = Animal("Bicho")
    a.falar()
    c = Cachorro("Rex")
    c.falar()
    g = Gato("Mimi")
    g.falar()
