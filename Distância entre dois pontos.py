#---------ENUNCIADO---------#

'''
Faça uma função que recebe 4 números, x1, y1, x2, y2, e devolve a distância entre os pontos (x1,y1) e (x2,y2).

O nome da sua função deve ser distancia_euclidiana.
'''

#----------CÓDIGO-----------#

from math import sqrt
def distancia_euclidiana (x1,y1,x2,y2):
    distancia = (sqrt(((x2-x1)**2) + ((y2-y1)**2)))
    return distancia

a=10
b=5
c=7
d=3
dist = distancia_euclidiana (a,b,c,d)
print (dist)
