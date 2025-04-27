# Exibir um poema com data e metadados usando args e kwargs
def exibir_poema(data_extenso, *args, **kwargs): # função para exibir poema
    # data_extenso: string com a data em formato longo
    texto = "\n".join(args) # junta os argumentos em uma string separada por nova linha
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()]) # junta os metadados em uma string separada por nova linha
    # kwargs: dicionário com os metadados (autor, ano, etc.)
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}" # formata a mensagem com a data, o poema e os metadados
    # exibe a mensagem formatada
    print(mensagem) # fim da função exibir_poema
# fim da função exibir_poema

# Exemplo de uso da função exibir_poema
exibir_poema(
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters", # autor do poema
    ano=2004, # ano de publicação do poema
    ano=1999, # ano de publicação do poema
    tema="Python", # tema do poema
    estilo="Programação", # estilo do poema
    tipo="Poema", # tipo do poema
    linguagem="Python", # linguagem do poema
    versao="3.10", # versão do Python
    data="2023-10-01", # data de publicação do poema 
    data_extenso="01 de Outubro de 2023", # data em formato longo
)