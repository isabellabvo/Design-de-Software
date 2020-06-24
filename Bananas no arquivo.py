  
#---------ENUNCIADO---------#

'''
Faça um programa que abre um arquivo texto chamado macacos-me-mordam.txt e imprime o número de ocorrências da palavra 'banana'. 
Atenção: palavras com letra maiúscula também devem ser contabilizadas, ou seja, se as palavras aparecerem assum: 'Banana', 'BANANA', 'BaNaNa', devem ser contadas como palavras. 
Exemplo de texto: 'Banana nanica banana da terra.'

'''

#----------CÓDIGO-----------#
quantidade = 0
with open("macacos-me-mordam.txt", "r") as arquivo:
    conteudos = arquivo.read()
lista = conteudos.split()
for palavra in lista:
    if palavra.upper() == "BANANA":
        quantidade+=1
print(quantidade)
