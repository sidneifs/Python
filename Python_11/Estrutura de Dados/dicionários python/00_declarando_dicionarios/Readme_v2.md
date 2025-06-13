# Dicionários em Python

> **Nota sobre versões:**
> Este material é uma versão revisada e aprimorada do conteúdo anterior sobre dicionários em Python, com exemplos práticos, tabelas explicativas e dicas para facilitar o aprendizado. Os arquivos desta pasta apresentam conceitos fundamentais e aplicações reais de dicionários, ideais para estudantes e iniciantes em programação.

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
```

---

## Principais métodos e funções de dicionários

| Método/Função   | Descrição                                              | Exemplo de uso                              |
|-----------------|--------------------------------------------------------|---------------------------------------------|
| get()           | Retorna o valor da chave ou valor padrão se não existir| pessoa.get("nome", "Não existe")           |
| items()         | Retorna pares (chave, valor)                           | pessoa.items()                              |
| keys()          | Retorna as chaves                                      | pessoa.keys()                               |
| values()        | Retorna os valores                                     | pessoa.values()                             |
| pop()           | Remove e retorna o valor de uma chave                  | pessoa.pop("idade")                        |
| popitem()       | Remove e retorna o último par adicionado               | pessoa.popitem()                            |
| update()        | Atualiza o dicionário com outro                        | pessoa.update({"telefone": "1234"})       |
| fromkeys()      | Cria novo dicionário com chaves de uma lista           | dict.fromkeys(["a", "b"], 0)              |
| setdefault()    | Retorna valor da chave ou define valor padrão          | pessoa.setdefault("email", "não informado")|
| clear()         | Remove todos os pares chave-valor                      | pessoa.clear()                              |
| copy()          | Cria uma cópia superficial do dicionário               | novo = pessoa.copy()                        |

---

## Exemplo prático: Cadastro de profissionais da aviação

```python
pessoas = [
    {
        "nome": "Carlos Silva",
        "idade": 45,
        "cargo": "Piloto",
        "atividade": "Pilota aeronaves comerciais",
        "cidade": "São Paulo",
        "empresa": "LATAM",
        "veiculo": "Carro",
        "salario": 18000.00,
        "participacao_lucros": 12.5
    },
    {
        "nome": "Fernanda Souza",
        "idade": 34,
        "cargo": "Comissária de Bordo",
        "atividade": "Atende passageiros durante voos",
        "cidade": "Rio de Janeiro",
        "empresa": "GOL",
        "veiculo": "Metrô",
        "salario": 6500.00,
        "participacao_lucros": 8.0
    },
    {
        "nome": "João Pereira",
        "idade": 29,
        "cargo": "Mecânico de Manutenção",
        "atividade": "Realiza manutenção em aeronaves",
        "cidade": "Campinas",
        "empresa": "Azul",
        "veiculo": "Moto",
        "salario": 7200.00,
        "participacao_lucros": 6.5
    },
    {
        "nome": "Marina Costa",
        "idade": 41,
        "cargo": "Controladora de Voo",
        "atividade": "Controla tráfego aéreo",
        "cidade": "Brasília",
        "empresa": "Infraero",
        "veiculo": "Carro",
        "salario": 12000.00,
        "participacao_lucros": 10.0
    },
    {
        "nome": "Eduardo Lima",
        "idade": 37,
        "cargo": "Engenheiro de Voo",
        "atividade": "Supervisiona sistemas de bordo",
        "cidade": "Porto Alegre",
        "empresa": "Avianca",
        "veiculo": "Bicicleta",
        "salario": 9500.00,
        "participacao_lucros": 7.2
    }
]

# Exemplo de acesso:
for pessoa in pessoas:
    print(f"{pessoa['nome']} trabalha como {pessoa['cargo']} na {pessoa['empresa']} e ganha R$ {pessoa['salario']:.2f}")
```

---

### Tabela explicativa do exemplo

| Nome            | Idade | Cargo                   | Atividade                        | Cidade         | Empresa  | Veículo   | Salário (R$) | % PLR |
|-----------------|-------|-------------------------|----------------------------------|----------------|----------|-----------|--------------|-------|
| Carlos Silva    | 45    | Piloto                  | Pilota aeronaves comerciais      | São Paulo      | LATAM    | Carro     | 18000.00     | 12.5  |
| Fernanda Souza  | 34    | Comissária de Bordo     | Atende passageiros durante voos  | Rio de Janeiro | GOL      | Metrô     | 6500.00      | 8.0   |
| João Pereira    | 29    | Mecânico de Manutenção  | Realiza manutenção em aeronaves  | Campinas       | Azul     | Moto      | 7200.00      | 6.5   |
| Marina Costa    | 41    | Controladora de Voo     | Controla tráfego aéreo           | Brasília       | Infraero | Carro     | 12000.00     | 10.0  |
| Eduardo Lima    | 37    | Engenheiro de Voo       | Supervisiona sistemas de bordo   | Porto Alegre   | Avianca  | Bicicleta | 9500.00      | 7.2   |

---

## Dicas

- Use dicionários para representar entidades com propriedades variadas.
- Aproveite os métodos para manipular, acessar e atualizar dados de forma eficiente.
- Dicionários são mutáveis e, a partir do Python 3.7+, preservam a ordem de inserção das chaves.

---

Agradeço por utilizar este material!

Sidnei Silva (sidneifs)
