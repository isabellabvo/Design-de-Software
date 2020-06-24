  
#---------ENUNCIADO---------#

'''
Desenvolva em Python uma função que recebe como argumento o número de elementos que serão usados na série e retorna o valor estimado de π.
Atenção, para esse exercício você deverá usar a estratégia apresentada para realizar o cálculo de π, outras estratégias não serão aceitas, e o valor retornado da função deve ser π (ou o valor aproximado alcançado pelo cálculo).

O nome da sua função deve ser PiWallis.
'''

#----------CÓDIGO-----------#

def PiWallis(n):
    metadedepi = 1
    for i in range (1,n+1):
        if i%2 == 0:
            numero = (i)/(i+1)
        elif i%2 != 0:
            numero = (i+1)/i
        metadedepi *=numero
    pi = 2 * metadedepi
    return pi
