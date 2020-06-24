#---------ENUNCIADO---------#

'''
Escreva um programa que pergunta a distância que um passageiro deseja percorrer em km.
Seu programa deve imprimir o preço da passagem, cobrando R$0.50 por km para viagens de até 200km e R$0.45 por quilômetro extra para viagens mais longas.
(Adaptado do ex. 4.6 livro Nilo Ney).

O resultado deve ser impresso com exatamente duas casas decimais.
'''

#----------CÓDIGO-----------#
a = float(input("Qual a distância que você deseja percorrer, em km?"))
if a <= 200:
          b = 0.50 * a
else:
          b = (0.50 * 200) + (0.45 * (a-200))

print ("R${0:.2f}".format(b))
