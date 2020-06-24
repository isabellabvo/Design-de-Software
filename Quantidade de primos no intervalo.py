#---------ENUNCIADO---------#

'''
Escreva uma função que recebe dois números a e b e devolve a quantidade de números de primos p tais que a≤p≤b.

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
    c=a
    num=0
    while c<= b:
        if eh_primo(c):
            num+=1
        c+=1
    return num
