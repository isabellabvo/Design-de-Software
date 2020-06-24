  
#---------ENUNCIADO---------#

'''
Foi criado um dicionário em Python para cada turma de design de software, o dicionário possui o nome do aluno e sua média final. Esses dicionários foram colocados em uma lista. Faça uma função recebe essa lista e calcule a média dos alunos de todas as turmas.

Por exemplo:

Para a lista alunos = [ {"aluno1": 5, "aluno2": 8}, {"aluno3": 5} ], a função calcula_media(alunos) retorna o valor 6.0

O nome da sua função deve ser calcula_media.
'''

#----------CÓDIGO-----------#

def calcula_media(alunos):
    soma = 0
    qnt = 0
    for i in alunos:
        for v in i.values():
            soma+=v
            qnt+=1
    media = soma/qnt
    return media
