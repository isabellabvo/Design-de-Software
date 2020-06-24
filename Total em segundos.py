#---------ENUNCIADO---------#

'''
Escreva um programa que pergunte, em sequência, uma quantidade de dias, horas, minutos e segundos para o usuário.
Depois calcule o total em segundos e imprima.
'''

#----------CÓDIGO-----------#
a = float (input ("Qual é a quantidade de dias?:"))
b = float (input ("Qual é a quantidade de horas?:"))
c = float (input ("Qual é a quantidade de minutos?:"))
d = float (input ("Qual é a quantidade de segundos?:"))
e = (a * 24 * 60 * 60) + (b*60*60) + (c*60) + d
print (e)
