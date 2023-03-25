# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1=float(input("Qual o valor do primeiro produto? R$"))
produto2=float(input("Qual o valor do segundo produto? R$"))
produto3=float(input("Qual o valor do terceiro produto? R$"))

def produto(P):
    print(f"O produto mais barato é o de que custa R${P:.2f}")

if produto1<produto2 and produto1<produto3:
    produto(produto1)
elif produto2<produto1 and produto2<produto3:
    produto(produto2)
elif produto3<produto1 and produto3<produto2:
    produto(produto3)

