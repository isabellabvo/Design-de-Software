#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma lista de listas e devolve uma lista simples composta por todos os elementos das listas originais. 
Ex: [[1, 2, 3], [4, 5, 6], [7, 8], [9], [10]] deve devolver [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

O nome da sua função deve ser junta_listas.

'''

#----------CÓDIGO-----------#
def junta_listas(lista):
    listacomp = []
    for i in range (len(lista)):
        listacomp.append([map(i.join, lista)])
    return listacomp
        
