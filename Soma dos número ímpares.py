#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma lista de números e devolve a soma dos números ímpares contidos nela.

O nome da sua função deve ser soma_impares.
'''

#----------CÓDIGO-----------#
#a = []
#def soma_impares(a):
    #i=0
    #while i < len(a):
        #if a[i] % 2 != 0:
            #a.append(i)
            #i+=1
        #else:
            #i+=1
    #return a

def soma_impares(a):
    soma=0
    for i in range(len(a)):
        b=a[i]
        if b%2 != 0:
            soma+=b
            print(soma)
            
    return soma
