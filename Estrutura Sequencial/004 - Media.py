#Faça um Programa que peça as 4 notas bimestrais e mostre a média.


# Cabeçalho
print("========================")
print(" CALCULADORA DE  MÉDIAS ")
print("========================")
print()

# Inputs
nome=input("DIGITE O NOME DO ALUNO: ")
print()

n1=float(input("DIGITE A PRIMEIRA NOTA: "))
n2=float(input("DIGITE A SEGUNDA NOTA: "))
n3=float(input("DIGITE A TERCEIRA NOTA: "))
n4=float(input("DIGITE A QUARTA NOTA: "))
print()

# Cálculo
media=(n1+n2+n3+n4)/4

# Impressão
print("===========")
print(f"| Nome: {nome}")
print(f"| Média: {media:.2f}")
print("===========")
print()