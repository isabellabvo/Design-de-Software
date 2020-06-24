#---------ENUNCIADO---------#

'''
Crie um programa que pergunta o nome do mês e imprime o número do mês (use os nomes dos meses com letra minúscula).
'''

#----------CÓDIGO-----------#
#c = input ("Qual o mês?")
#a = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
#b = [1,2,3,4,5,6,7,8,9,10,11,12]
#i=0
#while c != a[i]:
    #i+=1
#if a[i] == c :
    #print(b[i])
    
c = input ("Qual o mês?")
a = {"janeiro":1, "fevereiro":2, "março":3, "abril":4, "maio":5, "junho":6, "julho":7, "agosto":8, "setembro":9, "outubro":10, "novembro":11, "dezembro":12}

if c in a:
    l = a[c]
    print("O mês desse número é {}".format(l))
    
