#-------------ENUNCIADO-------------#

Escreva uma função que recebe um valor de distância, em km, percorrida por um veículo e o tempo gasto, em horas, para percorrer esta distância. 
A função retorna a velocidade média do veículo em km/h.
O nome da sua função deve ser calcula_velocidade_media.

#--------------CÓDIGO---------------#

def calcula_velocidade_media (valor_da_distancia, tempo_gasto):
    velocidade_media = valor_da_distancia/tempo_gasto
    return velocidade_media
a = 1000
b = 2
v_média = calcula_velocidade_media(a,b)
print (v_média)
