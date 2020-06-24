#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma lista de números e devolve outra lista contendo somente os números que formam uma sequência estritamente crescente a partir do primeiro elemento. 
O nome da sua função deve ser estritamente_crescente.
'''

#----------CÓDIGO-----------#
def estritamente_crescente(lista):
    listafinal = []
    for i in range (0, len(lista)):
        if i == 0:
            listafinal.append(lista[i])
        else: 
            if lista[i] > lista[i-1]:
                listafinal.append(lista[i])
        return listafinal
