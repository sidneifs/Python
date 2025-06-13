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