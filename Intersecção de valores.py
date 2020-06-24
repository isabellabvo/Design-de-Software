  
#---------ENUNCIADO---------#

'''
Faça uma função que recebe dois dicionários e devolve uma lista contendo os valores que estão presentes em ambos os dicionários.

O nome da sua função deve ser interseccao_valores.

'''

#----------CÓDIGO-----------#

def interseccao_valores(dic1,dic2):
    lista = []
    for a in dic1.values():
        if a in dic2.values():
            lista.append(a)
    return lista
