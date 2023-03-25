# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado=float(input("Digite o valor em centímetros do lado do quadrado: "))

area=lado**2
area_dobro=area*2

print(f"ÁREA DO QUADRADO: {area:.2f}")
print(f"DOBRO DA ÁREA DO QUADRADO: {area_dobro:.2f}")