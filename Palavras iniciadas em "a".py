#---------ENUNCIADO---------#

'''

Crie um programa que pergunte palavras ao usuário e preencha uma lista. O programa deve parar com a palavra "fim". 
Ao final, imprima somente as palavras em que a primeira letra seja "a". Use um print por palavra.
'''

#----------CÓDIGO-----------#
lista_com_as_palavras = []
a = input("Digite uma palavra")
while a != "fim":
    lista_com_as_palavras.append(a)
    a = input("Digite uma palavra")
i=0
while i < len(lista_com_as_palavras):
    f = lista_com_as_palavras[i]
    if f[0] == "a":
        print(f)
    i+=1
