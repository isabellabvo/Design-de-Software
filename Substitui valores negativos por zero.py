#---------ENUNCIADO---------#

'''
Faça uma função que varre uma lista de inteiros e troca os elementos negativos por zero. 
Sua função recebe uma lista como argumento e deve retornar a lista com os valores substituídos.

O nome da sua função deve ser zera_negativos.
'''

#----------CÓDIGO-----------#
def zera_negativos(a):
	i = 0
	while i < len(a):
		if a[i] < 0:
			a[i]=0
		i += 1
	return a
