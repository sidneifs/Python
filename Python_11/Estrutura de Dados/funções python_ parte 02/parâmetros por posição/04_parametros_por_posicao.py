# Parâmetros por posição
# Parâmetros por posição são aqueles que devem ser passados na ordem correta em que foram definidos na função.
# O operador `/` indica que os parâmetros anteriores a ele devem ser passados obrigatoriamente por posição.
# Os parâmetros após o `/` podem ser passados por nome (nomeados).

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    """
    Função para criar um carro com os dados fornecidos.

    Parâmetros:
    - modelo (str): Modelo do carro (obrigatório por posição).
    - ano (int): Ano de fabricação do carro (obrigatório por posição).
    - placa (str): Placa do carro (obrigatório por posição).
    - marca (str): Marca do carro (obrigatório por nome).
    - motor (str): Tipo de motor do carro (obrigatório por nome).
    - combustivel (str): Tipo de combustível do carro (obrigatório por nome).

    Retorno:
    - None. Apenas exibe os dados do carro.
    """
    print(f"Modelo: {modelo}, Ano: {ano}, Placa: {placa}, Marca: {marca}, Motor: {motor}, Combustível: {combustivel}")

# Exemplos de uso válidos:
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

# Exemplos de uso inválidos (comentados para evitar erros):
# criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")  # Inválido: 'marca', 'motor' e 'combustivel' devem ser nomeados.
# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", "1.0", combustivel="Gasolina")  # Inválido: 'motor' deve ser nomeado.
# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", "Gasolina")  # Inválido: 'combustivel' deve ser nomeado.