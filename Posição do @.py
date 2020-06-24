#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma string contendo um e-mail válido e retorna a posição do caractere '@'.

O nome da sua função deve ser pos_arroba.
'''

#----------CÓDIGO-----------#
def pos_arroba(str):
    a = str.find("@")
    return a
