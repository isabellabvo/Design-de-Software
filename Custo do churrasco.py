  
#---------ENUNCIADO---------#

'''
Um grupo de amigos gosta de fazer churrasco no final de semana e registra os custos do churrasco em um arquivo CSV onde cada linha contém o nome de um item de despesa, a quantidade consumida deste item e o seu custo unitário. 
Faça um programa que lê um arquivo chamado churras.txt, não necessariamente igual ao exemplo acima, e imprime o valor total dos custos do churrasco.
'''

#----------CÓDIGO-----------#

with open ("churras.txt", "r") as arquivo:
    lista = arquivo.readlines()
    for i, k in enumerate(lista):
        k += lista[i+1] * lista[i+2]
    print (k)    
