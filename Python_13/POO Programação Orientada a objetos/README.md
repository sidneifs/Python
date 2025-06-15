# Programação Orientada a Objetos (POO) em Python

## O que é POO?

A Programação Orientada a Objetos (POO) é um paradigma de programação baseado no conceito de "objetos", que podem conter dados (atributos) e código (métodos). POO facilita a organização, reutilização e manutenção do código, aproximando a lógica do programa do mundo real.

## Principais Conceitos

- **Classe:** Um molde/estrutura para criar objetos. Define atributos e métodos.
- **Objeto:** Uma instância de uma classe. Possui estado e comportamento.
- **Construtor:** Método especial (`__init__`) chamado ao criar um objeto.
- **Destrutor:** Método especial (`__del__`) chamado quando o objeto é destruído.
- **Herança:** Permite criar novas classes baseadas em outras, reutilizando código.
- **Polimorfismo:** Permite que diferentes classes implementem métodos com o mesmo nome, mas comportamentos distintos.
- **Atributos de classe e instância:** Atributos compartilhados por todas as instâncias (classe) ou exclusivos de cada objeto (instância).
- **Métodos de classe e estáticos:** Métodos que operam sobre a classe ou não dependem de instância.
- **Classes abstratas:** Classes que servem de base e não podem ser instanciadas diretamente.

## Exemplo Básico

```python
class Pessoa:
    def __init__(self, nome):  # Construtor
        self.nome = nome
        print(f"Pessoa {self.nome} criada.")
    def __del__(self):  # Destrutor
        print(f"Pessoa {self.nome} destruída.")
    def cumprimentar(self):
        print(f"Olá, meu nome é {self.nome}!")

p1 = Pessoa("Maria")
p1.cumprimentar()
```

## Como usar

1. Crie uma classe com atributos e métodos.
2. Instancie objetos dessa classe.
3. Use métodos para manipular os objetos.

## Aplicações

- Modelagem de sistemas bancários (contas, clientes, transações)
- Jogos (personagens, inimigos, itens)
- Sistemas de cadastro (usuários, produtos, pedidos)

---

## Exemplos Avançados

- Construtores e Destrutores: `poo_construtores_destrutores.py`
- Herança: `poo_heranca.py`
- Polimorfismo: `poo_polimorfismo.py`
- Atributos de classe e instância: `poo_atributos.py`
- Métodos de classe e estáticos: `poo_metodos.py`
- Classes abstratas: `poo_abstratas.py`
- Desafio Menu Bancário: `poo_menu_bancario.py`

Consulte cada arquivo para exemplos práticos e comentados.

---

Desenvolvido por Sidnei Silva (sidneifs)
