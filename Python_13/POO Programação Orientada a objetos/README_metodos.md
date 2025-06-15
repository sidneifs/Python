# Métodos de Classe e Métodos Estáticos em Python

Este exemplo mostra a diferença entre métodos de classe (`@classmethod`) e métodos estáticos (`@staticmethod`).

## O que são?

- **Método de classe:** Recebe a classe como primeiro argumento (`cls`). Pode acessar/modificar atributos da classe.
- **Método estático:** Não recebe referência à instância nem à classe. É como uma função comum dentro da classe.

## Exemplo de uso

```python
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

if __name__ == "__main__":
    c1 = ContaBancaria("Ana")
    c2 = ContaBancaria("João")
    print(f"Contas ativas: {ContaBancaria.contas_ativas()}")
    print(f"Banco: {ContaBancaria.banco()}")
```

## Saída esperada

```
Contas ativas: 2
Banco: Banco Python S.A.
```

- O método de classe acessa o atributo da classe.
- O método estático não depende de instância nem de classe.

---

Execute o arquivo `poo_metodos.py` para ver o exemplo na prática.
