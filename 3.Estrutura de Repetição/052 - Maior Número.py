#Faça um programa que leia 5 números e informe o maior número.

num1=int(input("Digite um número: "))
num_maior=num1
for c in range(1,5):
    if num1>num_maior:
        num_maior=num1
    num1=int(input("Digite um número: "))
print(f"O Maior número foi: {num_maior}")
