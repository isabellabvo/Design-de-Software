#---------ENUNCIADO---------#

'''
Faça uma função que recebe duas listas, uma de nomes e outra com os respectivos sobrenomes, e devolve uma nova lista com os nomes e sobrenomes em uma única string. 
Coloque exatamente um espaço entre o nome e o sobrenome.

O nome da sua função deve ser junta_nome_sobrenome.

'''

#----------CÓDIGO-----------#
def junta_nome_sobrenome(listanom,listasob):
    listafinal = []
    for i in range (0, len(listanom)):
        listafinal.append(listanom[i] + (" ") + listasob[i])
    return listafinal
