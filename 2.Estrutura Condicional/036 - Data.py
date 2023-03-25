#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

# Input
dia=int(input("DIGITE UM NÚMERO CORRESPONDENTE A UM DIA: "))
mes=int(input("DIGITE UM NÚMERO CORRESPONDENTE A UM MÊS: "))
ano=int(input("DIGITE UM NÚMERO CORRESPONDENTE A UM ANO: "))
print()

# IF's
if dia>31 or dia<1:
    print("O valor correspondente ao dia é invalido")
else:
    if mes>12 or mes<1:
        print("O valor correspondente ao mês é invalido")
    else:
        if ano<1 or ano>2023:
            print("O valor correspondente ao ano é invalido")
        else:
            print("A data é valida")
            print(f"DATA: {dia}/{mes}/{ano}")