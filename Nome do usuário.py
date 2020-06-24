#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma string contendo um e-mail válido e retorne o nome do usuário. Dica: use a função do exercício 62.

O nome da sua função deve ser nome_usuario.
'''

#----------CÓDIGO-----------#
def pos_arroba(str):
    a = str.find("@")
    return a
def nome_usuario(str):
    a = str[:pos_arroba(str)]
    return a
