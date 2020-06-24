  
#---------ENUNCIADO---------#

'''
Existe uma suspeita do laboratório SpuriousCorrelations de que a letra inicial do nome de um aluno influencia em seu desempenho acadêmico.
Faça uma função que recebe um dicionário de notas cujas chaves são os nomes dos alunos.
A função deve devolver um novo dicionário com as médias das notas dos alunos para cada letra inicial.

O nome da sua função deve ser medias_por_inicial.

'''

#----------CÓDIGO-----------#

def medias_por_inicial(dic):
    dicmedia = {}
    for nome in dic:
        if nome[0] in dicmedia:
            dicmedia[nome[0]] = (dicmedia[nome[0]] + dicmedia[nome])/2
        else:
            dicmedia[nome[0]] = dic[nome]
    return dic
