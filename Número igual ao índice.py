#---------ENUNCIADO---------#

'''
Faça uma função que recebe uma lista de números e devolve uma lista com os números que são iguais ao índice no qual eles se encontram.
O nome da sua função deve ser numero_no_indice.
'''

#----------CÓDIGO-----------#
#def numero_no_indice(a):
    #lista = [1,3,2,4]
    #c = []
    #while a != lista[a]:
        #return False
        #a+=1
    #while a == lista[a]:
        #return True
        #c.append(a) 
        #return c
    #return c
def numero_no_indice(a):
    listanova =[]
    for i in range (len(a)):
        if a[i]==i:
            listanova.append(a[i])
    return listanova
