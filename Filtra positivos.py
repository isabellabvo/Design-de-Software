#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma lista de números reais e retorna uma nova lista contendo apenas os números estritamente positivos da lista original.

O nome da sua função deve ser filtra_positivos.
'''

#----------CÓDIGO-----------#

def filtra_positivos(lista):
    novalista = []
    for i in range (len(lista)):
        if lista[i]> 0:
            novalista.append(lista[i])
    return novalista
