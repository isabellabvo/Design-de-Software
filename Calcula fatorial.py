#---------ENUNCIADO---------#

'''
Escreva uma função que recebe um número n e devolve o valor de n!=1⋅2⋅3⋯⋅n.
O nome da sua função deve ser fatorial.
'''

#----------CÓDIGO-----------#
#resultado=1
#numeros=1
#def fatorial(n):
	#resultado=1
	#numeros=1
	#while numeros <= n:
		#resultado *= numeros
		#numeros += 1
		#print (resultado)
	#return resultado

def fatorial(n):
    a=1
    for i in range (1, n+1):
        a*=i
        print (a)
    return a
    
