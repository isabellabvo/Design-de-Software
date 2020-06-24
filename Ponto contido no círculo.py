  
#---------ENUNCIADO---------#

'''
Crie uma classe chamada Circulo que tem na construção (no init ) um ponto como centro e um float como raio. Adicione um método contem(self, ponto) que avalia se um ponto está dentro da área do círculo ou não.

Pontos são representados por objetos da classe Ponto, especificada a seguir. Você não precisa implementar a classe Ponto.

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

'''

#----------CÓDIGO-----------#

class Circulo:
    def __init__(self, ponto, raio):
        self.centro = ponto
        self.r = raio
    def contem(self, outro_ponto):
        if (outro_ponto.x - self.centro.x)**2 +(outro_ponto.y - self.centro.y)**2 <= self.r**2:
            return True
