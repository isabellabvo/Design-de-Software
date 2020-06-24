  
#---------ENUNCIADO---------#

'''
Faça uma função que recebe os valores de n1, n2 e θ1 e retorna o valor do θ2. 
Os valores passados de n1, n2 são adimensionais, já os valores de θ1 e θ2 deverão ser recebidos e retornados em graus.

O nome da sua função deve ser snell_descartes.
'''

#----------CÓDIGO-----------#

import math
def snell_descartes(n1,n2,ang1): 
    ang2 = (n1 * (math.sin(math.radians(ang1)))) / n2
    return  math.degrees(math.asin(ang2))
