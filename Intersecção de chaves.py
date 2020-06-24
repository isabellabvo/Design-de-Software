  
#---------ENUNCIADO---------#

'''
Faça uma função que recebe dois dicionários e devolve uma lista contendo as chaves que estão presentes em ambos os dicionários.

O nome da sua função deve ser interseccao_chaves.
'''

#----------CÓDIGO-----------#

def interseccao_chaves(dic1,dic2):
    lista = []
    for a in dic1.keys():
        if a in dic2.keys():
            lista.append(a)
    return lista
