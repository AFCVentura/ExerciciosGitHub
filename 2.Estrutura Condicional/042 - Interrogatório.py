'''Exercicio 042
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: "Telefonou para a vítima?" "Esteve no local do crime?" "Mora perto da vítima?" "Devia para a vítima?" "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
# Inputs
print("==============================================")
interrogado=input("Digite seu nome: ")
print("--------------------")

print("RESPONDA TODAS AS PERGUNTAS COM 'S' PARA SIM E 'N' PARA NÃO")
pergunta1=input("Você telefonou para a vítima? ").upper()
pergunta2=input("Esteve no local do crime? ").upper()
pergunta3=input("Mora perto da vítima? ").upper()
pergunta4=input("Devia para a vítima? ").upper()
pergunta5=input("Já trabalhou com a vítima? ").upper()
print("==============================================")

# IF's
contagem=0
if pergunta1=="S":
    contagem+=1
if pergunta2=="S":
    contagem+=1
if pergunta3=="S":
    contagem+=1
if pergunta4=="S":
    contagem+=1
if pergunta5=="S":
    contagem+=1

if contagem<=1:
    status="INOCENTE"
elif contagem==2:
    status="SUSPEITO"
elif contagem<=4:
    status="CÚMPLICE"
elif contagem>=5:
    status="ASSASSINO"

print(f"{interrogado} é {status}")