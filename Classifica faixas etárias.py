  
#---------ENUNCIADO---------#

'''
Faça uma função que recebe um dicionário no qual as chaves são nomes de pessoas (representados por strings) e os valores são as idades de cada pessoa e retorna um novo dicionário no qual as chaves são faixas etárias e os valores são listas com os nomes das pessoas daquela faixa. Utilize a seguinte classificação:

Faixa etária	Idade
criança	11 anos ou menos
adolescente	Entre 12 e 17 anos
adulto	Entre 18 e 59 anos
idoso	60 anos ou mais

O nome da sua função deve ser agrupa_por_idade.

'''

#----------CÓDIGO-----------#

def agrupa_por_idade(dic):
    dicionariofinal = {'criança':[], 'adolescente':[], 'adulto': [], 'idoso': []}
    for k,v in dic.items():
        if v <= 11:
            dicionariofinal['criança'].append(k)
        elif 12 <= v <=17:
            dicionariofinal['adolescente'].append(k)
        elif 18 <= v <= 59:
            dicionariofinal['adulto'].append(k)
        elif v >= 60 :
            dicionariofinal['idoso'].append(k)
    return dicionariofinal
