  
#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma lista de números e retorna a string 'ímpar', 'par' ou 'misturado' se ela tiver, respectivamente, só números ímpares, só números pares, ou números dos dois tipos. Se a lista for vazia ela deve retornar misturado.

O nome da sua função deve ser verifica_lista.
'''

#----------CÓDIGO-----------#

def verifica_lista(listanum):
    if len(listanum) == 0:
        return "misturado"
    listapares = []
    listaimpares = []
    for i in range(len(listanum)):
        if listanum[i] %2 == 0:
            listapares.append(listanum[i])
        elif listanum[i] %2 != 0:
            listaimpares.append(listanum[i])     
    if listanum == listapares:
        return "par"
    elif listanum == listaimpares:
        return "ímpar"
    else:
        return "misturado"
