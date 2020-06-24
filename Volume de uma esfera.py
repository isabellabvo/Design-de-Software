#---------------ENUNCIADO----------------#

'''
Faça uma função que calcule o volume de uma esfera de raio R.

O nome da sua função deve ser calcula_volume_da_esfera.
'''

#----------------CÓDIGO------------------#

from math import pi
def calcula_volume_da_esfera (raio):
    volume = (4*pi*(raio**3))/3
    return volume

a=3
volume_esfera = calcula_volume_da_esfera(a)
print (volume_esfera)
