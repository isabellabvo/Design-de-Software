  
#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma string e retorna um dicionário com o número de ocorrências de cada bigrama (par de caracteres) dessa string.
O nome da sua função deve ser conta_bigramas.

'''

#----------CÓDIGO-----------#

def conta_bigramas(a):
    dicionario={}
    lista = []
    for bigrama in range(0, len(a)-1):
        lista.append(a[bigrama]+a[bigrama+1])
    for j in lista:
        if j in dicionario.keys():
            dicionario[j]+=1
        else:
            dicionario[j]=1
    return dicionario
