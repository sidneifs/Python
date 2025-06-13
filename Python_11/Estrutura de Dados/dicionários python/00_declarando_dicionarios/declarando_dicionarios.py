# Dicionários em Python
# Dicionários armazenam pares de chave-valor e são muito úteis para representar entidades com propriedades.

# Criando um dicionário
pessoa = {"nome": "Sidnei", "idade": 38}
print(pessoa)  # {'nome': 'Sidnei', 'idade': 38}

# Acessando valores
print(pessoa["nome"])  # Sidnei
print(pessoa["idade"])  # 38

# Adicionando ou atualizando valores
pessoa["telefone"] = "3375-4321"
print(pessoa)  # {'nome': 'Sidnei', 'idade': 38, 'telefone': '3375-4321'}
pessoa["idade"] = 39  # Atualizando idade
print(pessoa)  # {'nome': 'Sidnei', 'idade': 39, 'telefone': '3375-4321'}

# Verificando existência de chave
if "telefone" in pessoa:
    print("Telefone existe")  # Telefone existe

# Removendo um par chave-valor
del pessoa["telefone"]
print(pessoa)  # {'nome': 'Sidnei', 'idade': 39}

# Limpando o dicionário
pessoa.clear()
print(pessoa)  # {}

# Verificando se o dicionário está vazio
if not pessoa:
    print("Dicionário vazio")  # Dicionário vazio

# Copiando um dicionário
pessoa = {"nome": "Sidnei", "idade": 38}
novo_dicionario = pessoa.copy()
print(novo_dicionario)  # {'nome': 'Sidnei', 'idade': 38}

# Métodos úteis de dicionários:
# get() - Retorna o valor associado a uma chave, ou um valor padrão se a chave não existir.
print(pessoa.get("nome"))  # Sidnei
print(pessoa.get("telefone", "Não existe"))  # Não existe

# items(), keys(), values()
print(pessoa.items())   # dict_items([('nome', 'Sidnei'), ('idade', 38)])
print(pessoa.keys())    # dict_keys(['nome', 'idade'])
print(pessoa.values())  # dict_values(['Sidnei', 38])

# pop() - Remove e retorna o valor associado a uma chave.
print(pessoa.pop("idade"))  # 38
print(pessoa)  # {'nome': 'Sidnei'}

# popitem() - Remove e retorna o último par chave-valor adicionado.
print(pessoa.popitem())  # ('nome', 'Sidnei')
print(pessoa)  # {}

# update() - Atualiza o dicionário com pares de outro dicionário.
pessoa = {"nome": "Sidnei", "idade": 38}
pessoa.update({"telefone": "3375-4321"})
print(pessoa)  # {'nome': 'Sidnei', 'idade': 38, 'telefone': '3375-4321'}

# fromkeys() - Cria um novo dicionário com chaves de uma lista e valores padrão.
padrao = {}.fromkeys(["nome", "telefone"], "vazio")
print(padrao)  # {'nome': 'vazio', 'telefone': 'vazio'}

# setdefault() - Retorna o valor associado a uma chave, ou define um valor padrão se a chave não existir.
pessoa = {"nome": "Sidnei", "idade": 38}
print(pessoa.setdefault("telefone", "não informado"))  # não informado
print(pessoa)  # {'nome': 'Sidnei', 'idade': 38, 'telefone': 'não informado'}

# clear() - Remove todos os pares chave-valor do dicionário.
pessoa.clear()
print(pessoa)  # {}

# Comparando dicionários
pessoa1 = {"nome": "Sidnei", "idade": 38}
pessoa2 = {"nome": "Sidnei", "idade": 38}
print(pessoa1 == pessoa2)  # True (mesmo conteúdo)
print(pessoa1 is pessoa2)  # False (objetos diferentes)   
