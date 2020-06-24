#------------ENUNCIADO-------------#
'''
Faça uma função que calcule a posição de um objeto em movimento retilíneo uniforme em um instante t, com posição inicial s0 e velocidade v:

O nome da sua função deve ser calcula_posicao.
'''

#-------------CÓDIGO---------------#

def calcula_posicao (tempo, posição_inicial, velocidade):
    posição = posição_inicial + (velocidade*tempo)
    return posição

a= 15
b= 2
c= 20

posição_final = calcula_posicao (a,b,c)
print (posição_final)
