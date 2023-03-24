'''
Exercicio 043
Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
Álcool: até 20 litros, desconto de 3% por litro. acima de 20 litros, desconto de 5% por litro 
Gasolina: até 20 litros, desconto de 4% por litro. acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

# Cabeçalho
print("=========================================")
print("       P O S T O   I P I R A N G A       ")
print("=========================================")
print()

# Tabela de preços
print("=========================================")
print("             TABELA DE PREÇOS            ")
print("=========================================")
print("          GASOLINA:       R$2,50         ")
print("          ÁLCOOL:         R$1,90         ")
print("=========================================")
print("          Gasolina: -20l: 4% OFF         ")
print("          Gasolina: +20l: 6% OFF         ")
print("-----------------------------------------")
print("           Álcool: -20l: 3% OFF          ")
print("           Álcool: +20l: 5% OFF          ")
print("=========================================")
print()

# Input
print("=========================================")
print("| Qual combustível você deseja abastecer? ")
combustivel=input("| Digite G para gasolina e A para álcool: ").upper()
print("| Com quantos litros você deseja abastecer? ")
volume=float(input("| Desejo abastecer com: "))
print("=========================================")
print()
print()

# Atribuições
preco_gasolina=2.5
preco_alcool=1.9
if combustivel=="G":
    valor=preco_gasolina*volume
    if volume<20:
        valor=valor-(valor*0.04)
    elif volume>=20:
        valor=valor-(valor*0.06)
elif combustivel=="A":
    valor=preco_alcool*volume
    if volume<20:
        valor=valor-(valor*0.03)
    elif volume>=20:
        valor=valor-(valor*0.05)

# Impressão da nota
if combustivel=="G":
    comb_impress="Gasolina"
else:
    comb_impress="Álcool"
print("=========================================")
print(f"          Combustível: {comb_impress}   ")
print(f"          Volume: {volume:.1f} Litros   ")
print(f"          Preço Final: R${valor:.2f}    ")
print("=========================================")