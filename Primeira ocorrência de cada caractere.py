  
#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma string e devolve um dicionário com o índice da primeira ocorrência de cada caractere na string.

O nome da sua função deve ser primeiras_ocorrencias.

'''

#----------CÓDIGO-----------#

def primeiras_ocorrencias(a):
    dicionario = {}
    for i in a:
        if i not in dicionario:
            dicionario[i] = a[i]
    return dicionario
