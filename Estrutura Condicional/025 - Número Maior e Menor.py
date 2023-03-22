#Faça um Programa que leia três números e mostre o maior e o menor deles.


num1=int(input("DIGITE UM NÚMERO: "))
num2=int(input("DIGITE UM NÚMERO: "))
num3=int(input("DIGITE UM NÚMERO: "))
print()
def impressao_maior(N):
    print(f"O maior número é: {N}")

def impressao_menor(M):
    print(f"O menor número é: {M}")

if num1>num2 and num1>num3:
    impressao_maior(num1)
elif num2>num1 and num2>num3:
    impressao_maior(num2)
elif num3>num2 and num3>num1:
    impressao_maior(num3)
else: 
    print("ERRO")



if num1<num2 and num1<num3:
    impressao_menor(num1)
elif num2<num1 and num2<num3:
    impressao_menor(num2)
elif num3<num2 and num3<num1:
    impressao_menor(num3)
else: 
    print("ERRO")


