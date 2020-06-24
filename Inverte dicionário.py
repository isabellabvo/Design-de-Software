  
#---------ENUNCIADO---------#

'''
Escreva uma função que recebe um dicionário cujas chaves são nomes de pessoas (strings) e os valores são suas respectivas idades (números inteiros).
A função deve devolver um novo dicionário cujas chaves são idades e os valores são listas de strings com os nomes das pessoas que têm aquela idade.

O nome da sua função deve ser inverte_dicionario.

'''

#----------CÓDIGO-----------#

from collections import Counter, defaultdict

def inverte_dicionario(dic):
    dicionario_inv = defaultdict(list)
    for k, v in dic.items():
        dicionario_inv[v].append(k)
    return dicionario_inv
