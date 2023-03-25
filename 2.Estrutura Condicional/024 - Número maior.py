#Faça um Programa que leia três números e mostre o maior deles.

num1=int(input("DIGITE UM NÚMERO: "))
num2=int(input("DIGITE UM NÚMERO: "))
num3=int(input("DIGITE UM NÚMERO: "))
print()

if num1>num2 and num3:
    print(f"O maior número é: {num1}")
elif num2>num1 and num2>num3:
    print(f"O maior número é: {num2}")
elif num3>num2 and num3>num1:
    print(f"O maior número é: {num3}")
else: 
    print("ERRO")