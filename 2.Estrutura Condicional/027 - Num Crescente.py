#Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1=int(input("DIGITE O PRIMEIRO NÚMERO: "))
num2=int(input("DIGITE O SEGUNDO NÚMERO: "))
num3=int(input("DIGITE O TERCEIRO NÚMERO: "))
print()

if num1<num2<num3:
    print(f"{num1}<{num2}<{num3}")
elif num1<num3<num2:
    print(f"{num1}<{num3}<{num2}")
elif num2<num1<num3:
    print(f"{num2}<{num1}<{num3}")
elif num2<num3<num1:
    print(f"{num2}<{num3}<{num1}")
elif num3<num2<num1:
    print(f"{num3}<{num2}<{num1}")
elif num3<num1<num2:
    print(f"{num3}<{num1}<{num2}")
