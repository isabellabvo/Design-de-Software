  
#---------ENUNCIADO---------#

'''
Faça uma função que recebe um dicionário cujas chaves são nomes de pessoas e os valores são as respectivas datas de nascimento no formato 'dd/mm/aaaa', onde dd são dois caracteres representando o dia, mm são dois caracteres representando o mês e aaaa são quatro caracteres representando o ano. 
A função deve devolver um novo dicionário contendo somente os dados (nome e data de nascimento) dos aniversariantes de setembro.

O nome da sua função deve ser aniversariantes_de_setembro.

'''

#----------CÓDIGO-----------#

def aniversariantes_de_setembro(dic):
    dicionario ={}
    for p,n in dic.items():
        if n[3] == "0" and n[4] == "9":
            dicionario[p] = n
    return dicionario
