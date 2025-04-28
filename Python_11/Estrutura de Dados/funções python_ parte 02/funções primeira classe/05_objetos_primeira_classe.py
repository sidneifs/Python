# objetos primeira classe
# Funções são objetos de primeira classe em Python, o que significa que podem ser passadas como argumentos para outras funções, retornadas de outras funções e atribuídas a variáveis.
# Isso permite criar funções de ordem superior, que são funções que operam em outras funções, como map(), filter() e reduce().  
def somar(a, b): # função que soma dois números
    """Função que soma dois números."""
    # docstring é uma string que descreve a função e pode ser acessada através do atributo __doc__
    # A docstring deve ser a primeira linha da função e deve ser escrita entre aspas triplas.
    return a + b # retorna a soma de a e b

def subtrair(a, b): # função que subtrai dois números
    """Função que subtrai dois números."""
    return a - b # retorna a subtração de a e b 
def exibir_resultado(a, b, funcao): # função que exibe o resultado da operação
    """Função que exibe o resultado da operação."""
    resultado = funcao(a, b) # chama a função passada como argumento e armazena o resultado na variável resultado
    # A função pode ser qualquer função que receba dois argumentos e retorne um valor.
    print(f"O resultado da operação é = {resultado}") # exibe o resultado da operação
# A função exibir_resultado recebe dois números e uma função como argumentos e exibe o resultado da operação.
# A função pode ser qualquer função que receba dois argumentos e retorne um valor.

# Exemplo de uso da função exibir_resultado com a função subtrair como argumento
exibir_resultado(20, 10, subtrair)  # O resultado da operação 20 - 10 = 10
# Exemplo de uso da função exibir_resultado com a função somar como argumento

exibir_resultado(50, 1500, somar)  # O resultado da operação 50 + 1500 = 1550
# Exemplo de uso da função exibir_resultado com a função subtrair como argumento
exibir_resultado(10, 5, subtrair)  # O resultado da operação 10 - 5 = 5