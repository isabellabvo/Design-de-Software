  
#---------ENUNCIADO---------#

'''
Faça uma função que recebe duas listas com o mesmo tamanho e devolve um dicionário cujas chaves são os elementos da primeira lista e os valores são os elementos da segunda lista.
Para pensar: para a resolução deste exercício faz diferença saber qual o tipo dos valores guardados nas listas?

O nome da sua função deve ser monta_dicionario.
'''

#----------CÓDIGO-----------#

def monta_dicionario(a,b):
    dicionario = {}
    for i in range (len(a)):
        dicionario[a[i]] = b[i]
        print(dicionario)
    return dicionario
