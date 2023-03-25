'''Exercicio 038
Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

# Input
print("=============================================================================")
print("O caixa eletrônico aceita saques de valores inteiros entre R$10,00 e R$600,00")
saque=int(input("Digite o valor desejado para saque: "))
print("=============================================================================")
print()

# IF's
if saque<=600 and saque>=10:
    if saque>=100:
        nota100=saque//100
        if saque>=50:
            nota50=(saque-(nota100*100))//50
            nota10=(saque-(nota100*100)-(nota50*50))//10
            nota5=(saque-(nota100*100)-(nota50*50)-(nota10*10))//5
            nota1=(saque-(nota100*100)-(nota50*50)-(nota10*10)-(nota5*5))//1
        else:
            nota50=0
            nota10=(saque-(nota100*100)-(nota50*50))//10
            nota5=(saque-(nota100*100)-(nota50*50)-(nota10*10))//5   
            nota1=(saque-(nota100*100)-(nota50*50)-(nota10*10)-(nota5*5))//1         
    else:
        nota100=0
        if saque>=50:
            nota50=(saque-(nota100*100))//50
            nota10=(saque-(nota100*100)-(nota50*50))//10
            nota5=(saque-(nota100*100)-(nota50*50)-(nota10*10))//5
            nota1=(saque-(nota100*100)-(nota50*50)-(nota10*10)-(nota5*5))//1

        else:
            nota50=0
            nota10=(saque-(nota100*100)-(nota50*50))//10
            nota5=(saque-(nota100*100)-(nota50*50)-(nota10*10))//5 
            nota1=(saque-(nota100*100)-(nota50*50)-(nota10*10)-(nota5*5))//1
            
    #Impressão
    print("=======================================================================")
    print("O valor digitado precisará de:")
    if nota100>0:
        print(f"{nota100} notas de R$100")
    if nota50>0:
        print(f"{nota50} notas de R$50")
    if nota10>0:
        print(f"{nota10} notas de R$10")
    if nota5>0:
        print(f"{nota5} notas de R$5")
    if nota1>0:
        print(f"{nota1} notas de R$1")
    print("=======================================================================")
else:
    print("Digite um valor válido")


