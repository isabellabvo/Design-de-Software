  
#---------ENUNCIADO---------#

'''
Desenvolva um programa que imprima o ponto de maior erro da função de Bhāskara.
Para isso, para os valores de 0 a 90 graus, de um e um grau, analise a diferença da função de Bhāskara em relação a função math.sin do Python e diga qual é o valor em graus que o valor de seno apresenta a maior diferença entre ambas as técnicas.
Você provavelmente vai querer usar a função abs().

Importante: seu programa deve utilizar apenas um print.
'''

#----------CÓDIGO-----------#

import math
maior = 0
angulo = 0
for x in range (0,91):
    senodebaskara = (4*x*(180-x))/(40500-x*(180-x))
    senoreal = math.sin(math.radians(x))
    diferenca = abs(senodebaskara - senoreal)
    if diferenca > maior:
        maior = diferenca
        angulo = x
print (angulo)
