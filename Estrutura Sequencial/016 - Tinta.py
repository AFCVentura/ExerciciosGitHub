'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

metros_quadrados=int(input("QUANTIDADE DE M²: "))

litro=metros_quadrados/3
import math
lata=math.ceil(litro/18)
preco_lata=lata*80.00

print(f"QUANTIDADE DE LATAS: {lata:.2f}")
print(f"VALOR A SER PAGO: {preco_lata:.2f}")
