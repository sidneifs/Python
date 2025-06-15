# Exemplo de classe e objetos em Python
# Definição da classe Bicicleta
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
# Definição da classe Bicicleta
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1
    
# Método para buzinar a bicicleta
    def buzinar(self):
        print("Plim plim...")
        print("Bicicleta buzinando!")
# Método para parar a bicicleta
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")
# Método para correr com a bicicleta
    def correr(self):
        print("Vrummmmm...")    
        print("Bicicleta em movimento!")
# Método para imprimir o estado atual da bicicleta
    def imprimir(self):
        print(self.cor, self.modelo, self.ano, self.valor) # resultado em: vermelho caloi 2022 600
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")
# Método para imprimir o estado atual da bicicleta
    def imprimir(self):
        print(self.cor, self.modelo, self.ano, self.valor) # resultado em: vermelho caloi 2022 600
    def correr(self):
        print("Vrummmmm...")    
        print("Bicicleta em movimento!")
# Método para imprimir o estado atual da bicicleta   

    
    def __str__(self): # Método para representar a bicicleta como string
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("vermelha", "Caloi", 2025, 600) # Criação de um objeto da classe Bicicleta
print(b1)  # Imprime a representação da bicicleta
b1.buzinar() # Buzina a bicicleta
b1.correr() # Correr com a bicicleta
b1.parar() #
print(b1.cor, b1.modelo, b1.ano, b1.valor) # Imprime os atributos da bicicleta

# Criação de outro objeto da classe Bicicleta
b2 = Bicicleta("Verde", "Monark", 2000, 189) # Criação de outro objeto da classe Bicicleta
print(b2) # Imprime a representação da bicicleta
b2.buzinar() # Buzina a bicicleta
b2.correr() # Correr com a bicicleta
b2.parar() # Parar a bicicleta
print(b2.cor, b2.modelo, b2.ano, b2.valor) # Imprime os atributos da bicicleta
# Imprime os atributos da bicicleta
print(b1) # Imprime a representação da bicicleta
print(b2) # Imprime a representação da bicicleta
# Imprime a representação da bicicleta
print(b1 == b2) # Compara os objetos b1 e b2
# Compara os objetos b1 e b2
print(b1 == b1) # Compara os objetos b1 e b1 [True]
# Compara os objetos b1 e b1 [True]
print(b2 == b2) # Compara os objetos b2 e b2 [True]
# Compara os objetos b2 e b2 [True]
print(b1 == b2) # Compara os objetos b1 e b2 [False]
# Compara os objetos b1 e b2 [False]
# Imprime a representação da bicicleta

print(b1.__dict__) # Imprime o dicionário de atributos do objeto b1
print(b2.__dict__) # Imprime o dicionário de atributos do objeto b2
# Imprime o dicionário de atributos do objeto b1
print(b1.__dict__['cor']) # Imprime o valor do atributo 'cor' do objeto b1
print(b2.__dict__['cor']) # Imprime o valor do atributo 'cor' do objeto b2
# Imprime o valor do atributo 'cor' do objeto b1
print(b1.__dict__['modelo']) # Imprime o valor do atributo 'modelo' do objeto b1
print(b2.__dict__['modelo']) # Imprime o valor do atributo 'modelo' do objeto b2
# Imprime o valor do atributo 'modelo' do objeto b1
print(b1.__dict__['ano']) # Imprime o valor do atributo 'ano' do objeto b1

print(b2.__dict__['ano']) # Imprime o valor do atributo 'ano' do objeto b2
# Imprime o valor do atributo 'ano' do objeto b1
print(b1.__dict__['valor']) # Imprime o valor do atributo 'valor' do objeto b1

print(b2.__dict__['valor']) # Imprime o valor do atributo 'valor' do objeto b2
# Imprime o valor do atributo 'valor' do objeto b1
print(b1.__dict__['marcha']) # Imprime o valor do atributo 'marcha' do objeto b1
print(b2.__dict__['marcha']) # Imprime o valor do atributo 'marcha' do objeto b2
# Imprime o valor do atributo 'marcha' do objeto b1
print(b1.__dict__['marcha']) # Imprime o valor do atributo 'marcha' do objeto b1
print(b2.__dict__['marcha']) # Imprime o valor do atributo 'marcha' do objeto b2

#__ Dunder methods __eq__ and __ne__ for object comparison
#__dict__ é um dicionário que contém os atributos do objeto