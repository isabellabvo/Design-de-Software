#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma string e retorna o número de vezes em que a letra 'a' aparece nela.

O nome da sua função deve ser conta_a.

'''

#----------CÓDIGO-----------#
def conta_a(str):
    qnt = 0
    for i in str:
        if i == "a":
            qnt +=1
    return qnt        
    
