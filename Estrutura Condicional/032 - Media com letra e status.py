'''
Exercicio 032
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.

A atribuição de conceitos obedece à tabela abaixo: Média de Aproveitamento Conceito Entre 9.0 e 10.0 A Entre 7.5 e 9.0 B Entre 6.0 e 7.5 C Entre 4.0 e 6.0 D Entre 4.0 e zero E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

# Inputs
nome=input("Digite o nome do aluno: ")
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))

# Atribuição
media=(nota1+nota2)/2
if media>=9:
    media_letra="A"
elif media>=7.5:
    media_letra="B"
elif media>=6:
    media_letra="C"
elif media>=4:
    media_letra="D"
elif media>=0:
    media_letra="E"
else:
    print("ERRO")

if media_letra=="A" or media_letra=="B" or media_letra=="C":
    status="APROVADO"
elif media_letra=="D" or media_letra=="E":
    status="REPROVADO"

# Impressão
print("========================")
print(f"Nome: {nome}")
print(f"Média numérica: {media}")
print(f"Média em letra: {media_letra}")
print(f"Status: {status}")
print("========================")