  
#---------ENUNCIADO---------#

'''
Faça uma função que recebe 2 listas e retorna uma nova lista com os elementos da primeira lista que não estão na segunda lista.

Exemplo: para a entrada lista1 = [2, 7, 3.1, 'banana'] e lista2 = [2, 'banana', 'carro'] sua função deve devolver a lista [7, 3.1].

Atenção, esse é só um exemplo, sua função deve conseguir lidar com quaisquer listas de entrada e não apenas com as do exemplo.

O nome da sua função deve ser subtracao_de_listas.

'''

#----------CÓDIGO-----------#

def subtracao_de_listas (lista1,lista2):
    listafinal = lista1
    for i in lista1:
        if i in lista2:
            listafinal.remove(i)
    return listafinal
