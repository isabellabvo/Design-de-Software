#---------ENUNCIADO---------#

'''
Escreva uma função que recebe uma string e devolve uma lista com todos os seus sufixos.
Um sufixo é qualquer substring que se encontra no final da string original.
O nome da sua função deve ser lista_sufixos.

'''

#----------CÓDIGO-----------#
def  lista_sufixos(palavra):
    a = []
    for i in range(len(palavra)):
        t = palavra[i:]
        a.append(t)
    return a
