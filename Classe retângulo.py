  
#---------ENUNCIADO---------#

'''
Crie uma classe Retangulo, com um construtor (__init__) que recebe dois pontos e os armazena como atributos:

Ponto do canto inferior esquerdo
Ponto do canto superior direito
Cada ponto é um objeto do tipo Ponto, como definido à seguir:

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
Assuma que a classe Ponto já está definida, você só precisa implementar a classe Retangulo.

Sua classe Retangulo deve possuir dois métodos sem argumentos adicionais (lembre-se que métodos sempre recebem self):

calcula_perimetro(self): calcula o perímetro do retângulo;
calcula_area(self): calcula a área do retângulo.
'''

#----------CÓDIGO-----------#

class Retangulo:
    def __init__(self, inferior_esquerdo, superior_direito):
        self.inferior_esquerdo = inferior_esquerdo
        self.superior_direito = superior_direito
       
    def calcula_perimetro(self):
        x = self.inferior_esquerdo.x
        y = self.inferior_esquerdo.y
        a = self.superior_direito.x
        b = self.superior_direito.y
       
        dx = a - x
        dy  = b - y
       
       
        return (2*dx  + 2*dy)
    def calcula_area(self):
        x = self.inferior_esquerdo.x
        y = self.inferior_esquerdo.y
        a = self.superior_direito.x
        b = self.superior_direito.y
       
        dx = a - x
        dy  = b - y
       
        return (dx*dy)
