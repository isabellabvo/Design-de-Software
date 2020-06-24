#---------ENUNCIADO---------#

'''
Escreva um programa que pergunta uma palavra para o usuário até que ele acerte a senha ("desisto").
Quando o usuário acertar a senha, imprima "Você acertou a senha!".
'''

#----------CÓDIGO-----------#
a = input("Digite uma palavra:")
while a != "desisto":
    a = input("Digite uma palavra:")
if a == "desisto":
    print ("Você acertou a senha!")
