#---------ENUNCIADO---------#

'''
Escreva uma função que recebe um vetor de dimensão arbitrária representado por uma lista e devolve a sua norma. 
Caso seja necessário, pesquise por norma ou módulo de um vetor no Google ;)

O nome da sua função deve ser calcula_norma.
'''

#----------CÓDIGO-----------#
def calcula_norma(vet):
    for i in vet:
        for c in i:
            a = vet[c]
            b = vet[c+1]
            norma = (a**2+b**2)**1/2
    return norma
