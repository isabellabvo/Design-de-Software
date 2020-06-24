#---------ENUNCIADO-------#

'''
Faça uma função que recebe dois números, a e b, e devolve a raíz da equação ax+b=0.

O nome da sua função deve ser resolve_equacao_1o_grau.
'''

#---------CÓDIGO---------#

def resolve_equacao_1o_grau (a,b):
    y=-b/a
    return y

k=10
l=100
equacao = resolve_equacao_1o_grau (k,l)
print (equacao)
