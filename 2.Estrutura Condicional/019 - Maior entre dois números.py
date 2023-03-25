#Faça um Programa que peça dois números e imprima o maior deles.

numero1=int(input("DIGITE UM NÚMERO: "))
numero2=int(input("DIGITE OUTRO NÚMERO: "))

if numero1>numero2:
    print(f"O maior número é {numero1}")
elif numero1<numero2:
    print(f"O maior número é {numero2}")
elif numero1==numero2:
    print("Ambos os números são iguais")
else:
    print("ERRO")