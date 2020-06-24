#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma lista e devolve a lista invertida. Observação: a sua solução não pode usar slicing ou alguma outra função pronta do Python.

O nome da sua função deve ser inverte_lista.
'''

#----------CÓDIGO-----------#
def inverte_lista(lista):
    i = 0
    while i < (len(lista) - 1):
        lista.insert(i, lista.pop())
        i += 1
    return lista
