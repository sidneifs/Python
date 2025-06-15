# Exemplo: Métodos de Classe e Métodos Estáticos em Python

class ContaBancaria:
    total_contas = 0

    def __init__(self, titular):
        self.titular = titular
        ContaBancaria.total_contas += 1

    @classmethod
    def contas_ativas(cls):
        return cls.total_contas

    @staticmethod
    def banco():
        return "Banco Python S.A."

# Exemplo de uso
if __name__ == "__main__":
    c1 = ContaBancaria("Ana")
    c2 = ContaBancaria("João")
    print(f"Contas ativas: {ContaBancaria.contas_ativas()}")
    print(f"Banco: {ContaBancaria.banco()}")
