# Herança em Python

Este exemplo demonstra como funciona a herança em classes Python, permitindo criar novas classes baseadas em outras e reutilizar código.

## O que é Herança?

Herança é o mecanismo pelo qual uma classe (filha) pode herdar atributos e métodos de outra classe (pai), podendo também sobrescrever ou estender comportamentos.

## Exemplo de uso

```python
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

if __name__ == "__main__":
    a = Animal("Bicho")
    a.falar()
    c = Cachorro("Rex")
    c.falar()
    g = Gato("Mimi")
    g.falar()
```

## Saída esperada

```
Bicho faz um som.
Rex diz: Au Au!
Mimi diz: Miau!
```

- `Cachorro` e `Gato` herdam de `Animal` e sobrescrevem o método `falar`.
- O polimorfismo permite que cada classe filha tenha seu próprio comportamento para o mesmo método.

---

Execute o arquivo `poo_heranca.py` para ver o exemplo na prática.
