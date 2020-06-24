#---------ENUNCIADO---------#

'''
Faça uma função que recebe dois números a e b e devolve uma lista com todos os números primos p tais que a≤p≤b em ordem crescente.

O nome da sua função deve ser primos_entre.
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
