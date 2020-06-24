#---------ENUNCIADO---------#
'''
Escreva uma função que recebe um número representando um ano e devolve True se um ano é bissexto e False caso contrário.

O nome da sua função deve ser eh_bissexto.
'''

#----------CÓDIGO----------#

def eh_bissexto (a):
    if a%4 != 0:
        return False
    if a%100 !=0 :
        return True
    elif a%400 == 0:
        return True
    else:
        return False
