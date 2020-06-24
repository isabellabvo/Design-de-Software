  
#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma lista de palavras e retorna um dicionário onde as chaves são as palavras, e o valor é a contagem de cada palavra. Por exemplo, se a lista for

['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']
a função deve retornar

{'chuchu': 2, 'abobora': 3}
O nome da sua função deve ser conta_ocorrencias.
'''

#----------CÓDIGO-----------#

def conta_ocorrencias(a):
    dicionario={}
    for palavra in a:
        if palavra in dicionario.keys():
            dicionario[palavra]+=1
        else:
            dicionario[palavra] = 1
    return dicionario
