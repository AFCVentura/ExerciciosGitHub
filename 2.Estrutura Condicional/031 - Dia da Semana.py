'''
Exercicio 031
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''

# Input
num_dia=int(input("Digite um número de 1 a 7: "))

# If's
if num_dia==1: 
    dia="Domingo"
    print(f"O dia correspondente ao número {num_dia} é {dia}")
elif num_dia==2: 
    dia="Segunda-Feira"
    print(f"O dia correspondente ao número {num_dia} é {dia}")
elif num_dia==3: 
    dia="Terça-Feira"
    print(f"O dia correspondente ao número {num_dia} é {dia}")
elif num_dia==4: 
    dia="Quarta-Feira"
    print(f"O dia correspondente ao número {num_dia} é {dia}")
elif num_dia==5: 
    dia="Quinta-Feira"
    print(f"O dia correspondente ao número {num_dia} é {dia}")
elif num_dia==6: 
    dia="Sexta-Feira"
    print(f"O dia correspondente ao número {num_dia} é {dia}")
elif num_dia==7: 
    dia="Sábado"
    print(f"O dia correspondente ao número {num_dia} é {dia}")
else:
    print("ERRO")