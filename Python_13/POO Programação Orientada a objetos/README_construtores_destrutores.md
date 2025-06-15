# Construtores e Destrutores em Python

Este exemplo demonstra como funcionam os construtores (`__init__`) e destrutores (`__del__`) em classes Python.

## O que são?

- **Construtor:** Método chamado automaticamente ao criar um novo objeto. Usado para inicializar atributos.
- **Destrutor:** Método chamado quando o objeto é removido da memória (normalmente ao final do programa ou com `del`).

## Exemplo de uso

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(f"[Construtor] Pessoa {self.nome} criada com {self.idade} anos.")
    def apresentar(self):
        print(f"Olá! Eu sou {self.nome} e tenho {self.idade} anos.")
    def __del__(self):
        print(f"[Destrutor] Pessoa {self.nome} foi removida da memória.")

if __name__ == "__main__":
    p1 = Pessoa("Ana", 30)
    p1.apresentar()
    del p1
```

## Saída esperada

```
[Construtor] Pessoa Ana criada com 30 anos.
Olá! Eu sou Ana e tenho 30 anos.
[Destrutor] Pessoa Ana foi removida da memória.
```

- O construtor inicializa os atributos e exibe mensagem ao criar o objeto.
- O destrutor exibe mensagem ao remover o objeto.

---

Execute o arquivo `poo_construtores_destrutores.py` para ver o exemplo na prática.
