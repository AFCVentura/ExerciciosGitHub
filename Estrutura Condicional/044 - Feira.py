'''Exercicio 044
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

# Inputs
print("Preço da Maçã: R$1,80")
maca=float(input("Quantos KG você deseja comprar? "))
print("Preço do Morango: R$2,50")
morango=float(input("Quantos KG você deseja comprar? ")) 

# Atribuições
if maca<5:
    preco_maca=1.8*maca
elif maca>=5:
    preco_maca=1.5*maca

if morango<5:
    preco_morango=2.5*morango
elif morango>=5:
    preco_morango=2.2*morango

peso=maca+morango
preco=preco_morango+preco_maca

if peso>=8 or preco>=25:
    preco-=(preco*0.1)


# Impressão
print(f"KG de maçã: {maca} KG")
print(f"KG de morango: {morango} KG")
print(f"Preço Final: R${preco}")