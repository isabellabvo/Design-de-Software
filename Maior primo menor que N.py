#---------ENUNCIADO---------#

'''
Escreva uma função que recebe um número inteiro n e devolve o maior número primo menor ou igual a n.
Caso não haja nenhum número primo que se encaixe nessa situação (ex: números negativos), devolva -1.
Dica: Escreva uma função auxiliar que devolve True se o número é primo e False caso contrário.

O nome da sua função deve ser maior_primo_menor_que.

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

def maior_primo_menor_que(n):
    for c in range(n, 0, -1):
        if eh_primo(c):
            return c
    return -1
