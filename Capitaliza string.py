#---------ENUNCIADO---------#

'''
Escreva uma função que recebe uma string e devolve a versão capitalizada dessa string, ou seja, devolve a mesma string com a primeira letra maiúscula.
O nome da sua função deve ser capitaliza.
'''

#----------CÓDIGO-----------#
def capitaliza(string):
    stringcapitalizada = string[0].upper() + string[1:]
    return stringcapitalizada
