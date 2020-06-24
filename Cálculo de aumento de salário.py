#---------ENUNCIADO---------#

'''
Escreva uma função que recebe o salário atual do funcionário e calcule o valor do aumento. 
Para salários superiores a R$1.250,00, calcule um aumento de 10%. 
Para inferiores ou iguais, de 15% 
(Adaptado do ex. 4.4 livro Nilo Ney).

O nome da sua função deve ser calcula_aumento.
'''

#----------CÓDIGO-----------#

def calcula_aumento(a):
    if a > 1250:
        y= 0.1*a
        return(y)
    else:
        y= 0.15*a
        return(y)
