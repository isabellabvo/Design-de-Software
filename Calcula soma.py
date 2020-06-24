#---------ENUNCIADO---------#

'''
Escreva um programa que pergunta números para o usuário e, depois que o usuário digita o número 0 (zero), imprime a soma.


'''

#----------CÓDIGO-----------#
a = float (input("Digite números:"))
s=0 
while a != 0:
    s+=a
    a = float (input("Digite números:"))
if a == 0:
    print (s)
