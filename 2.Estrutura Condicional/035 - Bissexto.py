#Exercicio 035
# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

# Inputs
ano=int(input("Digite um ano: "))

# Bissexto
if ano%4==0:
    print(f"O ano {ano} é um ano bissexto")
else:
    print(f"O ano {ano} não é um ano bissexto")