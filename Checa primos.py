  
#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma lista de números e devolve um dicionário no qual as chaves são os números da lista e os valores são um booleano indicando se aquele número é primo ou não.

O nome da sua função deve ser verifica_primos.
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

def verifica_primos(lista):
    primos = {}
    for i in lista:
        primos[i] = eh_primo(i)
    return primos
