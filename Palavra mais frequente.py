  
#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma lista de palavras e retorna a palavra mais frequente. Por exemplo, para a lista

['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu’]
sua função deve retornar 'abobora'.

O nome da sua função deve ser mais_frequente.

'''

#----------CÓDIGO-----------#

def mais_frequente(a):
    dicionario = {}
    for palavra in a:
        if palavra in dicionario.keys():
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    p = 0
    c = 0
    for palavra, num in dicionario.items():
        if p < num:
            p = num
            c = palavra
           
    return c
