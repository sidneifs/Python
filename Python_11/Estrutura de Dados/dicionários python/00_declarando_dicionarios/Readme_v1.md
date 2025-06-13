# Dicionários em Python

Dicionários são estruturas de dados que armazenam pares de chave-valor. Eles são ideais para representar entidades com propriedades variadas e permitem acesso rápido aos valores por meio das chaves.

---

## Como criar e manipular dicionários

```python
# Criando um dicionário
pessoa = {"nome": "Sidnei", "idade": 38}

# Acessando valores
print(pessoa["nome"])  # Sidnei

# Adicionando ou atualizando valores
pessoa["telefone"] = "3375-4321"
pessoa["idade"] = 39

# Removendo um par chave-valor
del pessoa["telefone"]

# Limpando o dicionário
pessoa.clear()
