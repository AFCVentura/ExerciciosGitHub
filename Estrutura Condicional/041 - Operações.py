# Exercicio 041
# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é: par ou ímpar; positivo ou negativo; inteiro ou decimal.

# Inputs Número
numero1=float(input("Digite o primeiro número: "))
numero2=float(input("Digite o segundo número: "))
print()

# Input Operação
operacao=input("Qual operação você deseka realizar [+ - * /]? ")

#IF's operação
if operacao=="+" or operacao=="soma":
    resultado=numero1+numero2
elif operacao=="-" or operacao=="subtração":
    resultado=numero1-numero2
elif operacao=="*" or operacao=="multiplicação":
    resultado=numero1*numero2
elif operacao=="/" or operacao=="divisão":
    resultado=numero1/numero2

# IF's Resultado
    # IF Par ou Ímpar
if resultado%2==0:
    par_impar="PAR"
else:
    par_impar="ÍMPAR"
    # IF Positivo ou Negativo
if resultado>0:
    pos_neg="POSITIVO"
elif resultado<0:
    pos_neg="NEGATIVO"
else:
    pos_neg="NEUTRO"
    # IF Inteiro ou Decimal
if resultado%1==0:
    int_float="INTEIRO"
else:
    int_float="DECIMAL"

# Impressão
print("=============================")
print(f"RESULTADO: {resultado}")
print(f"O resultado é um valor {par_impar}")
print(f"O resultado é um valor {pos_neg}")
print(f"O resultado é um valor {int_float}")
print("=============================")