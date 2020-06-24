#---------ENUNCIADO---------#

'''
Escreva uma função que recebe uma string e devolve uma lista com todos os seus bigramas. 
Note que cada bigrama deve aparecer somente uma vez na lista.
O nome da sua função deve ser acha_bigramas.
'''


#----------CÓDIGO-----------#
def acha_bigramas(string):
    listabigramas = []
    for i in range(1,len(string)):
        soma = string[i] + string[i-1]
        if soma not in listabigramas:
            listabigramas.append(soma)
    return listabigramas
        
