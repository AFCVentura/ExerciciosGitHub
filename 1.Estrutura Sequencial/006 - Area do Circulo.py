#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio=float(input("Digite o raio do círculo em centímetros: "))
print()

import math
pi=math.pi
area=pi*raio**2

print(f"A área do círculo cujo raio é {raio}cm corresponde a {area:.2f}cm")