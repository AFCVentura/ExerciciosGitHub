'''
Exercicio 033
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas: Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro; Triângulo Equilátero: três lados iguais; Triângulo Isósceles: quaisquer dois lados iguais; Triângulo Escaleno: três lados diferentes;
'''

# Inputs
lado1=float(input("Digite o primeiro lado do triângulo: "))
lado2=float(input("Digite o segundo lado do triângulo: "))
lado3=float(input("Digite o terceiro lado do triângulo: "))
print()

# Checagem
if lado1+lado2>lado3 and lado1+lado3>lado2 and lado2+lado3>lado1:
    print("os valores citados podem formar um triângulo.")
    if lado1!=lado2!=lado3:
        tipo="Escaleno"
        print(f"O tipo deste triângulo é {tipo}")
    elif lado1==lado2==lado3:
        tipo="Equilátero"
        print(f"O tipo deste triângulo é {tipo}")
    else:
        tipo="Isósceles"
        print(f"O tipo deste triângulo é {tipo}")
else:
    print("Os valores citados não possibilitam a existência de um triângulo")