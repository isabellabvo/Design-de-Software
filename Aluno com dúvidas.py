#---------ENUNCIADO---------#

'''
Faça um programa que pergunta ao aluno se ele tem dúvidas na disciplina. 
Se o aluno responder qualquer coisa diferente de "não", escreva "Pratique mais" e pergunte novamente se ele tem dúvidas.
Continue perguntando até que o aluno responda que não tem dúvidas. 
Finalmente, escreva "Até a próxima".

Seu programa deve imprimir as strings exatamente como descritas acima e nada mais.
'''

#----------CÓDIGO-----------#
a = input("Você tem dúvidas?")
while a != "não":
    print ("Pratique mais")
    a = input("Você tem dúvidas?")
print ("Até a próxima")
