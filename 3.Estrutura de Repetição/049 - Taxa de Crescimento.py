# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

# Cabeçalho
print("++++++++++++++++++++++++++++++++++")
print("   TAXA DE CRESCIMENTO MUNDIAL    ")
print("++++++++++++++++++++++++++++++++++")
print()

# Inputs
print("================================")
pais1=input("Digite o nome do primeiro país: ")
print("----------")
pop1=int(input("Digite a população do primeiro país: "))
print("----------")
taxa1=float(input("Digite a taxa de crescimento anual do primeiro país: "))
print("================================")
print()

print("================================")
pais2=input("Digite o nome do segundo país: ")
print("----------")
pop2=int(input("Digite a população do segundo país: "))
print("----------")
taxa2=float(input("Digite a taxa de crescimento anual do segundo país: "))
print("================================")
print()

# Decisões e Impressão
import os
anos_pass=0
if pop1<pop2:
    if taxa1<=taxa2:
        print("====================================================================================")
        print(f"{pais1} nunca terá a população maior que {pais2} se manter esta taxa de crescimento")
        print("====================================================================================")
    elif taxa1>taxa2:
        while pop1<pop2:
            pop1+=(pop1*(taxa1/100))
            pop2+=(pop2*(taxa2/100))
            anos_pass+=1
            os.system("cls")
            print("===========================")
            print(f"Anos passados: {anos_pass}")
            print(f"População {pais1}: {pop1}")
            print(f"População {pais2}: {pop2}")
            print("===========================")
elif pop1>pop2:
    if taxa1>=taxa2:
        os.system("cls")
        print("==============================================================================================")
        print(f"{pais2} nunca terá a população maior que {pais1} se ambos mantiverem esta taxa de crescimento")
        print("==============================================================================================")
    elif taxa1<taxa2:
        while pop2<=pop1:
            pop1+=(pop1*(taxa1/100))
            pop2+=(pop2*(taxa2/100))
            anos_pass+=1
            os.system("cls")
            print("===========================")
            print(f"Anos passados: {anos_pass}")
            print(f"População {pais1}: {pop1:.0f}")
            print(f"População {pais2}: {pop2:.0f}")
            print("---------------------------")
            if anos_pass==1:
                print(f"A população de {pais2} passará a de {pais1} em {anos_pass} ano")
            else:
                print(f"A população de {pais2} passará a de {pais1} em {anos_pass} anos")
            print("===========================")    
elif pop1==pop2:
    os.system("cls")
    print("====================================")    
    print("A população dos dois países é igual.")
    print("====================================")    