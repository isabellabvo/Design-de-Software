#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma lista e decide se a lista é estritamente crescente.
Em caso positivo a função deve devolver True, em caso negativo, False.

O nome da sua função deve ser eh_crescente.

'''

#----------CÓDIGO-----------#
def eh_crescente(a):
    a = [1,7,9,8]
    i = 0
    while a[i] < a[i+1] and i < len(a):
        return True
        i+=1
    return False
