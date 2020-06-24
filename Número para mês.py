#---------ENUNCIADO---------#

'''
Crie um programa que pergunta o número do mês e imprime o nome do mês.
'''

#----------CÓDIGO-----------#
a = int(input("Qual o número do mês?"))
lista = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
print (lista[a-1])
