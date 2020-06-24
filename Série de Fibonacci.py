#---------ENUNCIADO---------#

'''
Faça uma função que recebe um número inteiro n e devolve uma lista contendo os n primeiros números da sequência de Fibonacci. 
O nome da sua função deve ser calcula_fibonacci.

'''

#----------CÓDIGO-----------#
def calcula_fibonacci(n):
    listafinal = []
    f1 = 1 
    f2 = 1
    if (n == 1): 
        listafinal.append(1)
    for i in range (2, n):
        f1 = f2
        soma = f1+f2
        f2 = soma
        listafinal.append(soma)        
    return listafinal
 
