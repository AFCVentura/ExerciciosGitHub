# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: o produto do dobro do primeiro com metade do segundo. a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.


num1=int(input("DIGITE O PRIMEIRO NÚMERO: "))
num2=int(input("DIGITE O SEGUNDO NÚMERO: "))
num3=float(input("DIGITE O TERCEIRO NÚMERO: "))
print()


calc1=(num1*2)+(num2/2)
calc2=(num1*3)+num3
calc3=num3**3

print(f"Dobro do primeiro número + metade do segundo número: {calc1}")
print(f"Triplo do primeiro número + terceiro número: {calc2}")
print(f"Terceiro número elevado ao cubo: {calc3}")
