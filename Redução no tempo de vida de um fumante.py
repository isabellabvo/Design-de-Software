#---------ENUNCIADO---------#

'''
Escreva um programa que calcule a redução de tempo de vida de um fumante a partir do número de cigarros. 
Pergunte quantos cigarros ele fuma por dia e há quantos anos fuma.
Imprima o tempo de vida perdido em dias. 
Considere que um cigarro rouba 10 minutos de expectativa de vida.
'''

#----------CÓDIGO-----------#

a = float (input ("Quantos cigarros você fuma por dia?"))
b = float (input ("Há quantos anos você fuma?"))
           
total_cigarros_fumados = (b*365)* a
dias_perdidos = (total_cigarros_fumados * 10)/(24*60)

print ("Você perdeu dias", dias_perdidos, "de vida")
