#--------------ENUNCIADO----------------#
'''
Escreva uma função que recebe um número inteiro representando a idade de uma pessoa e devolve uma string conforme a seguinte regra: 
"crianca" se a pessoa tem até 11 anos, inclusive; "adolescente" se a pessoa tem entre 12 e 17 anos, inclusive; "adulto" se a pessoa tem 18 anos ou mais. 
Observação: note que "crianca" deve ser com "c" e não "ç".
O nome da sua função deve ser classifica_idade.
'''
#---------------CÓDIGO------------------#

def classifica_idade(a):
    if a <= 11:
        return "crianca"
        
    elif a >= 12 and a <= 17:
        return "adolescente"
            
    else:
        return "adulto"
