"""O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor.
    Acrescente 10% de folga e sempre arredonde os valores para cima,
    isto é, considere latas cheias."""

import math

metros_quadrados=float(input("METROS QUADRADOS: "))
print()
print()

litro=metros_quadrados/6
lata18=math.ceil(litro/18)
lata3_6=math.ceil(litro/3.6)
lata18_div=litro//18
lata3_6_div=math.ceil((litro%18)/3.6)
lata_dividida=lata18_div+lata3_6_div

valor_18=lata18*80.00
valor_3_6=lata3_6*25.00
valor_lata18_div=lata18_div*80.00
valor_lata3_6_div=lata3_6_div*25.00

print(f"Latas de 18 litros: {lata18}")
print(f"Valor das latas de 18 litros: {valor_18}")
print()

print(f"Latas de 3.6 litros: {lata3_6}")
print(f"Valor das latas de 3.6 litros: {valor_3_6}")
print()
print()

print(f"Latas de 18 litros divididas: {lata18_div}")
print(f"Latas de 3.6 litros divididas: {lata3_6_div}")
print()

print(f"Valor das latas de 18 litros divididas: {valor_lata18_div}")
print(f"Valor das latas de 3.6 litros divididas: {valor_lata3_6_div}")
print()