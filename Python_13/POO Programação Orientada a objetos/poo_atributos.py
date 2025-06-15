# Exemplo: Atributos de Classe e Instância em Python

class Carro:
    rodas = 4  # atributo de classe (compartilhado)
    def __init__(self, modelo):
        self.modelo = modelo  # atributo de instância (exclusivo)

# Exemplo de uso
if __name__ == "__main__":
    c1 = Carro("Fusca")
    c2 = Carro("Gol")
    print(f"{c1.modelo} tem {c1.rodas} rodas.")
    print(f"{c2.modelo} tem {c2.rodas} rodas.")
    Carro.rodas = 3  # altera o atributo de classe
    print(f"Agora todos os carros têm {c1.rodas} rodas.")
    c2.rodas = 6  # cria atributo de instância apenas para c2
    print(f"{c2.modelo} personalizado tem {c2.rodas} rodas.")
    print(f"{c1.modelo} ainda tem {c1.rodas} rodas.")
