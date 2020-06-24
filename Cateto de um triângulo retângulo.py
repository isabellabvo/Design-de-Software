#--------ENUNCIADO--------#

'''

Faça uma função que recebe a medida de um dos catetos e da hipotenusa de um triângulo retângulo e devolve o valor do outro cateto.

O nome da sua função deve ser encontra_cateto.

'''

#---------CÓDIGO----------#

from math import sqrt
def encontra_cateto (cateto, hipotenusa):
    catetu = sqrt (hipotenusa**2 - cateto**2)
    return catetu 

a=5
b=7
cat = encontra_cateto(a,b)
print (cat)
