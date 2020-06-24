  
#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma string e retorna um dicionário onde cada chave é uma letra da string, e cada valor é o número de ocorrências desta letra. Por exemplo, se passamos a string "banana nanica", a função devolve o dicionário:

{'b': 1, 'a': 5, 'n': 4, ' ': 1, 'i': 1, 'c': 1}
Nota importante: em geral as chaves do dicionário não estão ordenadas!

O nome da sua função deve ser conta_letras.

'''

#----------CÓDIGO-----------#

def conta_letras(a):
    dicionario = {}
    for c in a:
        if c  in dicionario.keys():
            dicionario[c]+=1
        else:
            dicionario[c] = 1
    return dicionario
