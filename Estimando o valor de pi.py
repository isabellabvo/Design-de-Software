  
#---------ENUNCIADO---------#

'''
Faça uma função que recebe o valor de n e retorna o resultado da fórmula acima utilizando os n termos.

O nome da sua função deve ser calcula_pi.
'''

#----------CÓDIGO-----------#
import math
def calcula_pi(n):
    valordepi = 0
    soma = 0
    for i in range (1,n+1):
        soma += (6/(i**2))
        valordepi = math.sqrt(soma)
        print(valordepi)
    return valordepi
