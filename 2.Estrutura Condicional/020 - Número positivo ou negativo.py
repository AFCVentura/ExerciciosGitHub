# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero1=int(input("DIGITE UM NÚMERO: "))
if numero1>0:
    print(f"O número {numero1} é positivo")
elif numero1<0:
    print(f"O número {numero1} é negativo")
elif numero1==0:
    print(f"O número {numero1} é nulo")
else: 
    print("ERRO")