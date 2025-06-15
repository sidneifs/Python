# Atributos de Classe e Instância em Python

Este exemplo mostra a diferença entre atributos de classe (compartilhados por todas as instâncias) e atributos de instância (exclusivos de cada objeto).

## O que são?

- **Atributo de classe:** Definido diretamente na classe, compartilhado por todas as instâncias.
- **Atributo de instância:** Definido no construtor (`__init__`), exclusivo de cada objeto.

## Exemplo de uso

```python
class Carro:
    rodas = 4  # atributo de classe
    def __init__(self, modelo):
        self.modelo = modelo  # atributo de instância

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
```

## Saída esperada

```
Fusca tem 4 rodas.
Gol tem 4 rodas.
Agora todos os carros têm 3 rodas.
Gol personalizado tem 6 rodas.
Fusca ainda tem 3 rodas.
```

- Alterar o atributo de classe afeta todas as instâncias, exceto as que já possuem o atributo sobrescrito.
- Atributos de instância são exclusivos de cada objeto.

---

Execute o arquivo `poo_atributos.py` para ver o exemplo na prática.
