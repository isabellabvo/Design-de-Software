  
#---------ENUNCIADO---------#

'''
Faça um programa que conta e imprime a quantidade de palavras em um arquivo chamado texto.txt (não contar espaços em branco).

Dica: use .split()
'''

#----------CÓDIGO-----------#
with open("texto.txt", "r") as arquivo:
    conteudos = arquivo.read()
lista = conteudos.split()
print(len(lista))
