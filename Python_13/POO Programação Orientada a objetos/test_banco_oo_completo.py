import unittest
from banco_oo_completo import Cliente, Conta, ContaCorrente, ContaPoupanca, Banco

class TestBancoOO(unittest.TestCase):
    def setUp(self):
        self.banco = Banco(arquivo_dados="test_banco.json")
        self.banco.clientes = []
        self.banco.contas = []

    def test_criar_cliente(self):
        self.banco.clientes = []
        cliente = Cliente("Teste", "12345678901", "senha")
        self.banco.clientes.append(cliente)
        self.assertEqual(len(self.banco.clientes), 1)
        self.assertEqual(self.banco.clientes[0].nome, "Teste")

    def test_criar_conta_corrente(self):
        cliente = Cliente("Teste", "12345678901", "senha")
        self.banco.clientes.append(cliente)
        conta = ContaCorrente(1, cliente)
        self.banco.contas.append(conta)
        cliente.adicionar_conta(conta)
        self.assertEqual(len(cliente.contas), 1)
        self.assertIsInstance(cliente.contas[0], ContaCorrente)

    def test_deposito_saque(self):
        cliente = Cliente("Teste", "12345678901", "senha")
        conta = ContaCorrente(1, cliente)
        conta.depositar(100)
        self.assertEqual(conta.saldo, 100)
        conta.sacar(50)
        self.assertEqual(conta.saldo, 50)
        conta.sacar(1000)  # Excede limite
        self.assertEqual(conta.saldo, 50)

    def test_historico_transacoes(self):
        cliente = Cliente("Teste", "12345678901", "senha")
        conta = ContaPoupanca(1, cliente)
        conta.depositar(200)
        conta.sacar(50)
        self.assertEqual(len(conta.transacoes), 2)
        self.assertEqual(conta.transacoes[0][0], "Depósito")
        self.assertEqual(conta.transacoes[1][0], "Saque")

if __name__ == "__main__":
    unittest.main()
