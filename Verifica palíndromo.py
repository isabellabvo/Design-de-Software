#---------ENUNCIADO---------#

'''

Faça uma função que recebe uma string e retorna True se ela for um palíndromo (é a mesma de trás para frente), ou False caso contrário
O nome da sua função deve ser eh_palindromo.
'''

#----------CÓDIGO-----------#

def eh_palindromo(frase):
    if frase[::-1] == frase[::1]:
        return True
    else:
        return False
    
