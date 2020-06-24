  
#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma lista de números e retorna a string 'crescente', 'decrescente' ou 'nenhum' se ela for, respectivamente, estritamente crescente, estritamente decrescente, ou nenhum dos dois (em algumas partes é crescente e em outras é decrescente).
Se a lista tiver menos de dois elementos ela deve retornar obrigatoriamente 'nenhum'.

O nome da sua função deve ser classifica_lista.
'''

#----------CÓDIGO-----------#

def classifica_lista(lista):
    if len(lista) < 2:
        return "nenhum"
    listacrescente = [lista[0]]
    listadecrescente = [lista[0]]
    maior = lista[0]
    menor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maior:
            listacrescente.append(lista[i])
            maior = lista[i]
        elif lista[i] < menor:
            listadecrescente.append(lista[i])
            menor = lista[i]
         
    if lista == listacrescente:
        return "crescente"
    elif lista == listadecrescente:
        return "decrescente"
    else:
        return "nenhum"
