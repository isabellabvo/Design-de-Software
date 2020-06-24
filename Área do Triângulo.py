#----------ENUNCIADO--------#
'''
Faça uma função que calcula a área de um triângulo de base b e altura h.

O nome da sua função deve ser calcula_area_do_triangulo.
'''

#----------CÓDIGO-----------#

def calcula_area_do_triangulo (b, h):
    area = (b*h)/2
    return area

a=10
b=5
area_do_triangulo = calcula_area_do_triangulo (a,b)
print (area_do_triangulo)
