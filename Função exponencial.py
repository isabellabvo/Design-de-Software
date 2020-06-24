  
#---------ENUNCIADO---------#

'''
Faça uma função em Python que calcula o resultado do ex para uma série de tamanho n. 
Você pode supor que as entradas para x e n serão enviadas nesta ordem e sempre serão números positivos.

O nome da sua função deve ser calcula_euler.
'''

#----------CÓDIGO-----------#

def calcula_euler(x,n):
    i = 0
    fatorial = 1
    e = 1 
    euler = 0
    while i < n:
        euler += (x**i)/fatorial
        i+=1
        fatorial*=e
        e+=1
    return euler
