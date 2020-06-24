  
#---------ENUNCIADO---------#

'''
Faça um programa que lê os nomes e o valor da aceleração de atletas digitados pelo usuário até que o nome digitado seja 'sair' (nesse caso o usuário digita 'sair' no nome e o programa não deve perguntar a aceleração).
O programa deve então usar a função do exercício 77 (repita a função na sua solução) para imprimir o nome do vencedor e o seu tempo de conclusão no formato: 'O vencedor é NOME com tempo de conclusão de TEMPO s' onde NOME é o nome do vencedor e TEMPO é o seu tempo de conclusão.
'''

#----------CÓDIGO-----------#

while True:
    nome = input("Digite um nome: ")
    if nome == "sair":
        break
    aceleracao = input("Qual aceleração? ")
    
def calcula_tempo(dic):
    dicionario = {}
    maior = 0
    for nome,aceleracao in dic.items():
        dicionario[nome] = ((200/aceleracao)**(1/2))
        for i in range (dicionario.values):
            if i > maior:
                maior = i
                pessoa = dicionario.keys
            
    return ('O vencedor é', pessoa, 'com tempo de conclusão de', i, 's')
