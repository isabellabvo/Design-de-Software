#---------ENUNCIADO--------#
'''
Faça uma função que calcule a distância alcançada por um projétil lançado com velocidade v em um ângulo θ, de uma altura y0. A distância é dada pela fórmula:
Use g=9.8.

O nome da sua função deve ser calcula_distancia_do_projetil.
'''

#----------CÓDIGO----------#

import math
g=9.8
def calcula_distancia_do_projetil (v,angulo,altura):
    d = ((v**2)/(2*g))*(1+ math.sqrt(1+ ((2*g*altura)/((v**2)*(math.sin(angulo)**2)))))*math.sin(angulo*2)
    return d
a=10
b=7
c=5
distancia = calcula_distancia_do_projetil (a,b,c)
print (distancia)
