  
#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma string composta somente por letras minúsculas e a devolve removendo as vogais.

O nome da sua função deve ser remove_vogais.
'''

#----------CÓDIGO-----------#

def remove_vogais(string):
    stringsemvogal = string
    vogais = ('a', 'e', 'i', 'o', 'u')
    for i in string:
        if i in vogais:
            stringsemvogal = stringsemvogal.replace(i,"")
    return stringsemvogal
