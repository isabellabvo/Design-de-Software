#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma senha (string) e devolve uma string do mesmo tamanho da senha formada somente por asteriscos ('*').

O nome da sua função deve ser esconde_senha.

'''

#----------CÓDIGO-----------#

def esconde_senha(string):
    nova = ''
    for i in string:
        nova = string.replace(string[i],'*')
    return nova
