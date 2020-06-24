#---------ENUNCIADO---------#
'''
Escreva um programa que pergunta para o usuário o valor da conta do restaurante e imprime:
"Valor da conta com 10%: R$ X.YZ", onde X.YZ é um número com exatamente duas casas decimais.
'''
#----------CÓDIGO-----------#
a = float(input("Qual o valor da conta do restaurante?"))
b = a + (a * 0.10)

print ("Valor da conta com 10%: R$ {0:.2f}".format(b))
