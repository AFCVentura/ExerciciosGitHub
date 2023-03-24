'''Exercicio 042
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: "Telefonou para a vítima?" "Esteve no local do crime?" "Mora perto da vítima?" "Devia para a vítima?" "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
# Inputs
print("==============================================")
interrogado=input("Digite seu nome: ")
print("--------------------")
print()

print("RESPONDA TODAS AS PERGUNTAS COM 'S' PARA SIM E 'N' PARA NÃO")
pergunta1=input("Você telefonou para a vítima? ")
pergunta2=input("Esteve no local do crime? ")
pergunta3=input("Mora perto da vítima? ")
pergunta4=input("Devia para a vítima? ")
pergunta5=input("Já trabalhou com a vítima? ")
print("==============================================")
lista_perguntas=[pergunta1,pergunta2,pergunta3,pergunta4,pergunta5]

if "N" in lista_perguntas==5 or "N" in lista_perguntas==4:
    status="INOCENTE"
elif "N" in lista_perguntas==3:
    status="SUSPEITO"
elif "N" in lista_perguntas==2 or "N" in lista_perguntas==1:
    status="CÚMPLICE"
elif "N" in lista_perguntas==0:
    status="ASSASSINO"

print(status)