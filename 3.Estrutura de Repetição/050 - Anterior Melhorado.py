# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.


# Cabeçalho
print("++++++++++++++++++++++++++++++++++")
print("   TAXA DE CRESCIMENTO MUNDIAL    ")
print("++++++++++++++++++++++++++++++++++")
print()

# Decisões e Impressão
import os
conti="Y"
anos_pass=0
while conti=="Y":
    os.system("cls")
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
    while pop1<=0:
        print("----------")
        pop1=int(input("Digite uma população válida para o primeiro país: "))
        print("----------")
        print()
    while pop2<=0:
        print("----------")
        pop2=int(input("Digite uma população válida para o segundo país: "))
        print("----------")
        print()
    if pop1<pop2:
        if taxa1<=taxa2:
            os.system("cls")
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
    conti=input("Deseja refazer a simulação? [Y/N] ").upper()   