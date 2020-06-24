#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma lista de números reais e retorna a soma de seus valores.

O nome da sua função deve ser soma_valores.

'''

#----------CÓDIGO-----------#
#a = [1, 2, 3, 4]

#def soma_valores(a):
    #i = 0
    #soma_valores = 0
    #b = len(a)
    #while i < b:
        #soma_valores += a[i]
        #i+=1
    #return soma_valores

def soma_valores(a):
    somavalores = 0
    for i in range (len(a)):
        somavalores += a[i]
        print (somavalores)
    return somavalores
