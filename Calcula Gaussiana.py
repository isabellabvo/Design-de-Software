#---------------ENUNCIADO----------------#
'''
Faça uma função que recebe 3 números reais como argumento: x, μ (mi) e σ (sigma). 
Essa função deve retornar o valor da seguinte fórmula:
O nome da sua função deve ser calcula_gaussiana.
'''
#---------------CÓDIGO-------------------#

from math import e, sqrt, pi

def calcula_gaussiana (x, mi, sigma):
    y = (1/(sqrt(2*pi)*sigma))*e**(-0.5*((x-mi)/(sigma))**2)
    return y
a= 0
b= 0
c= 1/(sqrt(2*pi))

gauss = calcula_gaussiana(a,b,c)
print (gauss)
