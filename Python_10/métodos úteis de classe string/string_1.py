nome = "sIdnEi sILVa"   # string de exemplo
print(nome[0])  # imprime o primeiro caractere da string
print(nome[-1]) # imprime o último caractere da string 
print(nome[0:4]) # imprime os caracteres do índice 0 ao 3 (não inclui o índice 4)
print(nome[0:4:2]) # imprime os caracteres do índice 0 ao 3, pulando de 2 em 2
print(nome[:]) # imprime toda a string
print(nome[::-1]) # imprime a string ao contrário
print(len(nome)) # imprime o tamanho da string
print(nome.count("i")) # conta quantas vezes a letra "i" aparece na string
print(nome.count("i", 0, 10)) # conta quantas vezes a letra "i" aparece na string do índice 0 ao 9
print(nome.find("i")) # encontra o índice da primeira ocorrência da letra "i"
print(nome.find("i", 0, 10)) # encontra o índice da primeira ocorrência da letra "i" do índice 0 ao 9
print(nome.find("z")) # retorna -1 se a letra "z" não estiver na string
print(nome.index("i")) # encontra o índice da primeira ocorrência da letra "i"
print(nome.index("i", 0, 10)) # encontra o índice da primeira ocorrência da letra "i" do índice 0 ao 9
print(nome.isalpha()) # verifica se todos os caracteres são letras
print(nome.isalnum()) # verifica se todos os caracteres são letras ou números
print(nome.isnumeric()) # verifica se todos os caracteres são números
print(nome.isupper()) # verifica se todos os caracteres são maiúsculos
print(nome.islower()) # verifica se todos os caracteres são minúsculos
print(nome.isdigit()) # verifica se todos os caracteres são dígitos
print(nome.isdecimal()) # verifica se todos os caracteres são decimais
print(nome.isidentifier()) # verifica se a string é um identificador válido
print(nome.isprintable()) # verifica se todos os caracteres são imprimíveis
print(nome.isspace()) # verifica se todos os caracteres são espaços em branco
print(nome.istitle()) # verifica se a string é um título (primeira letra de cada palavra em maiúscula)
print(nome.isascii()) # verifica se todos os caracteres são ASCII
print(nome.capitalize()) # coloca a primeira letra em maiúscula e o restante em minúscula
print(nome.title()) # coloca a primeira letra de cada palavra em maiúscula
print(nome.swapcase()) # troca maiúsculas por minúsculas e vice-versa
print(nome.replace("i", "o")) # substitui todas as ocorrências da letra "i" por "o"
print(nome.replace("i", "o", 1)) # substitui a primeira ocorrência da letra "i" por "o"
print(nome.split()) # divide a string em uma lista de substrings
print(nome.split("i")) # divide a string em uma lista de substrings separadas pela letra "i"
print(nome.strip()) # remove espaços em branco no início e no final da string
print(nome.rstrip()) # remove espaços em branco no final da string
print(nome.lstrip()) # remove espaços em branco no início da string

print(nome.upper()) # converte a string para maiúsculas
print(nome.lower()) # converte a string para minúsculas
print(nome.title()) # converte a string para título (primeira letra de cada palavra em maiúscula)

texto = "  HElLo WoRlD!   "  # string de exemplo   

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Sidnei Silva" # string de exemplo
print(menu) # imprime o menu com letras minúsculas
print(menu.upper()) # imprime o menu com letras maiúsculas

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))

print(nome.index("z")) # retorna um erro se a letra "z" não estiver na string