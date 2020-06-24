#---------ENUNCIADO---------#

'''
Crie um programa que pede ao usuário que digite números inteiros positivos e armazene-os em uma lista, até que o usuário digite um número negativo ou zero. 
Em seguida, imprima os números digitados na ordem reversa.
'''

#----------CÓDIGO-----------#
a = int (input("Qual o número:"))
b = []
while a > 0:
    b.append(a)
    a = int(input("Qual o número:"))
c = b[::-1]
print(c)
