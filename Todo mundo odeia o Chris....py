#------------ENUNCIADO-------------#
'''
Escreva um programa que pergunta o nome do usuário e imprime "Olá, NOME", onde NOME é o nome do usuário. 
A menos que o nome do usuário seja Chris. 
Neste caso, imprima "Todo mundo odeia o Chris".
'''

#------------CÓDIGO----------------#

a = input("Qual o seu nome?")
if a == "Chris":
    print ("Todo mundo odeia o Chris")
else:
    print ("Olá,", a)
