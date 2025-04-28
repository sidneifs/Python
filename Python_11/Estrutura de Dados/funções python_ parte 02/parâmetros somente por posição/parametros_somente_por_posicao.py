# Parâmetros somente por posição
# Parâmetros somente por posição são aqueles que não podem ser passados como argumentos nomeados.
# Eles devem ser passados apenas por posição, ou seja, na ordem em que foram definidos na função.

# Para definir um parâmetro como somente por posição, você deve usar uma barra (/) na definição da função.
# Isso indica que todos os parâmetros à esquerda da barra devem ser passados apenas por posição.    
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): # Parâmetros somente por posição
    print(modelo, ano, placa, marca, motor, combustivel) # Parâmetros somente por posição


# Exemplo de uso
criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")  # válido
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido