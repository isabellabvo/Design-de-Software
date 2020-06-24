#-----------ENUNCIADO-----------#
'''
Faça uma função que calcule o volume de uma pizza de raio z e altura a.
Assuma que a pizza é um cilindro.

O nome da sua função deve ser volume_da_pizza.
'''

#-----------CÓDIGO--------------#

from math import pi
def volume_da_pizza (raio, altura):
    volume_pizza = pi*(raio**2)*altura
    return volume_pizza
a=5
b=7
volume_cilindro = volume_da_pizza (a,b)
print (volume_cilindro)
