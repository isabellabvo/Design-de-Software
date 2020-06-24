#---------ENUNCIADO---------#

'''
Faça uma função que recebe os lados de um triângulo e retorna se ele é equilátero, isósceles ou escaleno. 
Sua função deve retornar a string "equilátero", "isósceles", ou "escaleno". Assuma que os lados do triângulo são válidos.

O nome da sua função deve ser classifica_triangulo.
'''

#----------CÓDIGO-----------#

def classifica_triangulo (a,b,c):
    if a==b==c:
        return ("equilátero")
    elif a==b or b==c or a==c:
        return ("isósceles")
    else:
        return ("escaleno")
 
