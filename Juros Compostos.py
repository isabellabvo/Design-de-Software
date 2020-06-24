#----------------ENUNCIADO----------------#
'''
Escreva uma função que calcula o valor devido ao final de um empréstimo. 
Os argumentos de entrada da função serão: valor emprestado, número de meses e taxa de juros. 
Atenção: usar juros compostos para calcular o valor devido.
O nome da sua função deve ser calcula_valor_devido.
'''
#-----------------CÓDIGO------------------#

def calcula_valor_devido (valor_emprestado, número_de_meses, taxa_de_juros):
    valor_final = valor_emprestado * (1 + taxa_de_juros)**número_de_meses
    return valor_final
a = 1000
b = 2
c = 0.2
empréstimo = calcula_valor_devido(a,b,c)
print (empréstimo)
