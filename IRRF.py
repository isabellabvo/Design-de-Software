  
#---------ENUNCIADO---------#

'''
Faça um programa que pergunta o salário bruto e o número de dependentes do usuário e imprime o seu Imposto de Renda Retido na Fonte (IRRF) simplificado. O cálculo do IRRF simplificado depende do valor da contribuição para o INSS e da base de cálculo. A contribuição para o INSS é dada pela tabela:

Faixa salarial	Alíquota
Até R$ 1.045,00	7,5%
De R$ 1.045,01 até R$ 2.089,60	9%
De R$ 2.089,61 até R$ 3.134,40	12%
De R$ 3.134,41 até R$ 6.101,06	14%
Acima de R$ 6.101,06	R$ 671,12 (valor fixo)
Por exemplo, se o salário bruto for R$ 2.000,00 a contribuição para o INSS será: 
2000×0.09=180.

A base de cálculo do IRRF simplificado é dada por:

Base de cálculo = salário bruto - contribuição para o INSS - número de dependentes X 189,59
Finalmente, o IRRF simplificado é dado por:

IRRF = Base de cálculo X alíquota - dedução
A alíquota e dedução podem ser obtidas na tabela a seguir, que depende da base de cálculo:

Base de cálculo	Alíquota	Dedução
Até R$ 1.903,98	0.0%	R$ 0,00
De R$ 1.903,99 até R$ 2.826,65	7,5%	R$ 142,80
De R$ 2.826,66 até R$ 3.751,05	15%	R$ 354,80
De R$ 3.751,06 até R$ 4.664,68	22,5%	R$ 636,13
Acima de R$ 4.664,68	27,5%	R$ 869,36
Exemplo (atenção, este é apenas um exemplo):

Para o salário bruto de R$ 10.000,00 e 2 dependentes, a contribuição para o INSS é 671,12, a base de cálculo é 10000−671,12−2×189,59=8949,70.
Finalmente, o IRRF simplificado é 8949,70×0,275−869,36=1591,8075.
Para o salário bruto de R$ 3.000,00 e nenhum dependente, a contribuição para o INSS é 3000×0,12=360, a base de cálculo é 3000−360−0×189,59=2640. 
Finalmente, o IRRF simplificado é 2640×0,075−142,80=55,20.
Fonte: https://www.calculadorafacil.com.br/trabalhista/calculo-salario-liquido
'''

#----------CÓDIGO-----------#

a = float(input("Qual o seu salário bruto?: "))
b = float(input("Qual o número de dependentes do usuário?: "))
contribuicao = 0
if a <= 1045:
    contribuicao = a * 0.075
    print("Essa {0} é a sua contribuição para o INSS!". format(contribuicao))

elif 1045.01 <= a<= 2089.60:
    contruibuicao = a * 0.09
    print("Essa {0} é a sua contribuição para o INSS!". format(contribuicao))
    
elif 2089.61 <= a <= 3134.40:
    contribuicao = a * 0.12
    print("Essa {0} é a sua contribuição para o INSS!". format(contribuicao))

elif 3134.41 <= a <= 6101.06:
    contribuicao = a * 0.14
    print("Essa {0} é a sua contribuição para o INSS!". format(contribuicao))

elif a>= 6101.67:
    contribuicao = 671.12

base_de_calculo = (a-contribuicao-b*189.59)
if base_de_calculo <= 1903.98:
    aliquota = 0
    deducao = 0
elif 1903.99 <= base_de_calculo <= 2826.65:
    aliquota = 0.075
    deducao = 142.80
elif 2826.66 <= base_de_calculo <= 3751.05:
    aliquota = 0.15
    deducao = 354.80
elif 3751.06 <= base_de_calculo <= 4664.68:
    aliquota = 0.225
    deducao = 636.13
elif base_de_calculo >= 4664.68:
    aliquota = 0.275
    deducao = 869.36
irff = base_de_calculo *aliquota - deducao
print (irff)
