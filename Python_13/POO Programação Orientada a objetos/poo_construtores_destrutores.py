# Exemplo: Construtores e Destrutores em Python

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(f"[Construtor] Pessoa {self.nome} criada com {self.idade} anos.")

    def apresentar(self):
        print(f"Olá! Eu sou {self.nome} e tenho {self.idade} anos.")

    def __del__(self):
        print(f"[Destrutor] Pessoa {self.nome} foi removida da memória.")

# Exemplo de uso
if __name__ == "__main__":
    p1 = Pessoa("Ana", 30)
    p1.apresentar()
    p2 = Pessoa("Carlos", 25)
    p2.apresentar()
    # Os destrutores serão chamados automaticamente ao final do programa ou quando os objetos forem deletados
    del p1
    print("Fim do exemplo.")
