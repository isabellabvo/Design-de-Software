  
#---------ENUNCIADO---------#

'''
Escreva uma função que recebe um número inteiro devolva a raiz_quadrada dele, para fazer essa conta use a estratégia de subtrações sucessivas. 
Suponha que o número informado é positivo e vai levar a uma raiz quadrada exata, ou seja não vai ser um número "quebrado". 
Para fazer esse cálculo, faça subtrações sucessiva dos números impares do valor pedido, o número de vezes é o valor desejado. 
Mais informações em: https://www.youtube.com/watch?v=w-tLphmhxkg

O nome da sua função deve ser raiz_quadrada.

'''

#----------CÓDIGO-----------#

x=1
x+=2
y=1
def raiz_quadrada(n):
    x=1
    x+=2
    y=1
    while y != 0:
        y = n - x
        print (y)
    return y
