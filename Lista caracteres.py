#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma string e devolve uma lista contendo os caracteres dessa string, sem repetição. 
Ex: 'abacate' deve devolver ['a', 'b', 'c', 't', 'e'].

O nome da sua função deve ser lista_caracteres.
'''

#----------CÓDIGO-----------#
def lista_caracteres(string):
    j = []
    for i in string:
        if i not in j:
            j.append(i)
    return j
