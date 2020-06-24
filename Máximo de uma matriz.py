#---------ENUNCIADO---------#

'''
Escreva uma função que recebe uma matriz de tamanho 3×3 e devolve o maior valor absoluto dentre todos os seus elementos. 
A matriz é representada por uma lista de listas
Curiosidade: o maior valor absoluto encontrado em uma matriz é conhecido como a norma infinito dessa matriz.

O nome da sua função deve ser encontra_maximo.
'''

#----------CÓDIGO-----------#
def encontra_maximo(matriz):
    valorabs = abs(matriz[0][0])
    for i in matriz:
        for c in i:
            if abs(c) > valorabs:
                valorabs = abs(c)
    return valorabs
