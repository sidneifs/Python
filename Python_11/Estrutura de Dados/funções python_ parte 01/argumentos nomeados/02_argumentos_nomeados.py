def salvar_carro(marca, modelo, ano, placa): # função para salvar carro
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}") # imprime os dados do carro
    return True # retorna verdadeiro se o carro foi salvo com sucesso
# fim da função salvar_carro
if __name__ == "__main__": # se o arquivo for executado diretamente
    salvar_carro("Fiat", "Palio", 1999, "ABC-1234") # chama a função salvar_carro com os argumentos
    # marca, modelo, ano e placa
salvar_carro("Fiat", "Palio", 1999, "ABC-1234") # chama a função salvar_carro com os argumentos
#1 marca, modelo, ano e placa
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") # chama a função salvar_carro com os argumentos
#2 marca, modelo, ano e placa
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) # chama a função salvar_carro com os argumentos
#3 marca, modelo, ano e placa