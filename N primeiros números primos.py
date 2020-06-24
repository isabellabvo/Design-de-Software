#---------ENUNCIADO---------#

'''
Escreva uma função que recebe um número n e retorna uma lista com os n primeiros números primos em ordem crescente (adaptado do Ex. 5.24 do livro do Nilo Ney).

O nome da sua função deve ser lista_primos.
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

def lista_primos(n):
	cont = 0
	lista = []
	i=2
	while cont < n:
		if eh_primo(i):
			lista.append(i)
			cont+= 1
		i+= 1
	return lista
