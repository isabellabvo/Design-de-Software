#---------ENUNCIADO---------#

'''
Faça um programa que determina qual número positivo inicial menor que 1000 gera a sequência de Collatz mais longa. Seu programa deve imprimir esse número.

Nota: Uma vez que a sequência começa os números podem passar de 1000.
'''

#----------CÓDIGO-----------#
def collatz(n):
    while n != 1:
        if n % 2 == 0:
            k = n / 2
            print(k)
        else:
            y = n * 3 + 1
            print(y)
