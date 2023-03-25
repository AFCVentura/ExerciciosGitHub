# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

fahrenheit=float(input("TEMPERATURA EM °F: "))

celsius= (5*(fahrenheit-32)/9)

print()

print(f"TEMPERATURA EM °C: {celsius:.1f}")
