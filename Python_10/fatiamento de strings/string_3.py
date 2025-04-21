nome = "Sidnei Ferreira da Silva" #fatiamento de strings
print(nome) #imprime a string

print(nome[0:5]) #do zero ao 5
print(nome[6:15]) #do 6 ao 15
print(nome[6:]) #do 6 ao final
print(nome[0:15:2]) #do 0 ao 15 de 2 em 2
print(nome[0:15:3]) #do 0 ao 15 de 3 em 3
print(nome[0:15:4]) #do 0 ao 15 de 4 em 4
print(nome[0:15:5]) #do 0 ao 15 de 5 em 5

print(nome[0]) #imprime o primeiro caractere
print(nome[-1]) #imprime o ultimo caractere 
print(nome[-2]) #imprime o penultimo caractere
print(nome[-3]) #imprime o antepenultimo caractere
print(nome[:9]) #imprime do 0 ao 9
print(nome[9:]) #imprime do 9 ao final
print(nome[10:]) #imprime do 10 ao final
print(nome[10:16]) #imprime do 10 ao 16
print(nome[10:16:1]) #imprime do 10 ao 16 de 1 em 1
print(nome[10:16:2]) #imprime do 10 ao 16 de 2 em 2
print(nome[:]) #imprime a string toda
print(nome[:15]) #imprime do 0 ao 15
print(nome[::-1]) #imprime a string ao contrario
print(nome[::-2]) #imprime a string ao contrario de 2 em 2
print(nome[::-3]) #imprime a string ao contrario de 3 em 3

print(len(nome)) #imprime o tamanho da string
print(nome.count('e')) #imprime quantas vezes o caractere 'e' aparece na string
print(nome.count('a')) #imprime quantas vezes o caractere 'a' aparece na string
print(nome.count('S')) #imprime quantas vezes o caractere 'S' aparece na string
print(nome.count('s')) #imprime quantas vezes o caractere 's' aparece na string
print(nome.count('F')) #imprime quantas vezes o caractere 'F' aparece na string
print(nome.count('f')) #imprime quantas vezes o caractere 'f' aparece na string
print(nome.count('i')) #imprime quantas vezes o caractere 'i' aparece na string
print(nome.count('I')) #imprime quantas vezes o caractere 'I' aparece na string
print(nome.count(' ')) #imprime quantas vezes o caractere ' ' aparece na string
print(nome.count('')) #imprime quantas vezes o caractere '' aparece na string

print(nome.find('e')) #imprime a posição do primeiro caractere 'e'  na string
print(nome.find('a')) #imprime a posição do primeiro caractere 'a'  na string
print(nome.find('S')) #imprime a posição do primeiro caractere 'S'  na string
print(nome.find('s')) #imprime a posição do primeiro caractere 's'  na string
print(nome.find('F')) #imprime a posição do primeiro caractere 'F'  na string
print(nome.find('f')) #imprime a posição do primeiro caractere 'f'  na string
print(nome.find('i')) #imprime a posição do primeiro caractere 'i'  na string
print(nome.find('I')) #imprime a posição do primeiro caractere 'I'  na string
print(nome.find(' ')) #imprime a posição do primeiro caractere ' '  na string
print(nome.find('')) #imprime a posição do primeiro caractere ''  na string
print(nome.find('x')) #imprime a posição do primeiro caractere 'x'  na string
print(nome.find('X')) #imprime a posição do primeiro caractere 'X'  na string
print(nome.find('y')) #imprime a posição do primeiro caractere 'y'  na string
print(nome.find('Y')) #imprime a posição do primeiro caractere 'Y'  na string

print(nome.replace('F', 'f')) #substitui o caractere 'F' por 'f' na string
print(nome.replace('f', 'F')) #substitui o caractere 'f' por 'F' na string

print(nome.upper()) #imprime a string em maiusculo
print(nome.lower()) #imprime a string em minusculo
print(nome.title()) #imprime a string em maiusculo com a primeira letra de cada palavra em maiusculo
print(nome.capitalize()) #imprime a string em maiusculo com a primeira letra em maiusculo
print(nome.strip()) #remove os espaços em branco do inicio e do final da string
print(nome.lstrip()) #remove os espaços em branco do inicio da string
print(nome.rstrip()) #remove os espaços em branco do final da string
print(nome.split()) #divide a string em uma lista de strings
print(nome.split('e')) #divide a string em uma lista de strings a partir do caractere 'e'

print(nome.split(' ')) #divide a string em uma lista de strings a partir do caractere ' '

