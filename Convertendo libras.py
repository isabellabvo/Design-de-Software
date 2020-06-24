#-----------ENUNCIADO------------#

'''
Faça uma função que recebe um peso em libras e devolve o seu equivalente em quilogramas. Considere 6 casas decimais.

O nome da sua função deve ser libras_para_kg.

'''

#-------------CÓDIGO-------------#

def libras_para_kg (libras):
    kg = libras * 0.453592
    return kg
a = 100
kilograma = libras_para_kg (a)
print (kilograma)
