#---------ENUNCIADO---------#

'''
Faça uma função que recebe 4 números, x1, y1, x2, y2, e devolve a distância entre os pontos (x1,y1) e (x2,y2).
O nome da sua função deve ser distancia_euclidiana.
'''

#----------CÓDIGO-----------#
def eh_primo (num):
	i=2
	if num == 2:
		return True
	elif num == 0 or num == 1:
		return False
	while i < num:
		if num % i == 0:
			return False
		i = i+1
	return True

def primos_entre(a,b):
    primos = []
    for cont in range (a,b+1):
        if eh_primo(cont):
            primos.append(cont)
    return primos  
