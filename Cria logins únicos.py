  
#---------ENUNCIADO---------#

'''
Faça um programa que pergunta logins para o usuário até que ele digite a palavra 'fim'. Para cada login digitado pelo usuário, o programa deve verificar qual é o próximo login disponível no sistema e adicionar esse novo login em uma lista. Ao final do programa, os login devem ser impressos, um por linha, no console.

Utilize a função do Exercício 168.

Exemplo de interação com o programa:

Usuário digita: fabio
Usuário digita: andre
Usuário digita: fabio
Usuário digita: fabio
Usuário digita: fim
Programa imprime: fabio
Programa imprime: andre
Programa imprime: fabio1
Programa imprime: fabio2
A ordem em que os logins são impressos não importa.
'''

#----------CÓDIGO-----------#

def login_disponivel(login, listalog):
    c = 1
    if login not in listalog:
            return login
    else:
        for i in range (len(listalog)):
            while login in listalog:
                login += str(c)
                if login in listalog:
                    login = login[:-1]
                    c+=1
            return login
        
listalogin = []
while True:
    loginusuario = input("Digite um login: ")  
    if loginusuario == "fim":
        break
    else:
        final = login_disponivel(loginusuario, listalogin)
        listalogin.append(final)
print(listalogin)
