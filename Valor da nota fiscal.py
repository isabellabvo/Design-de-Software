#---------ENUNCIADO---------#

'''
Faça uma função que recebe duas listas com informações de uma nota fiscal e devolve o preço total da nota. A nota fiscal é representada pelas duas listas, uma com preços de produtos e outra com a respectiva quantidade de itens comprados daquele produto.

O nome da sua função deve ser calcula_total_da_nota.

'''

#----------CÓDIGO-----------#
def calcula_total_da_nota (preço, quant):
    pfinal = 0
    for i in range(len(preço)):
        pfinal += preço[i]*quant[i]      
    return pfinal
