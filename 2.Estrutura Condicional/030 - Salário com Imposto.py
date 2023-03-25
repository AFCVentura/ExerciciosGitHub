""" Imposto de renda
<=900: n tem
900<x>=1500: 5%
1500<x>=2500: 10%
2500<x:20%
INSS:10%
FGTS:11% mas não é descontado """

#Cabeçalho
print("===================================")
print("       C A L C U L A D O R A       ")
print("                D E                ")
print("          S A L Á R I O S          ")        
print("===================================")
print()

#Inputs
print("-----------------------")
hora=int(input("HORAS TRABALHADAS: "))
print()

valor=int(input("PAGAMENTO POR HORA: "))
print("-----------------------")
print()


#calculos imposto de renda
salario_bruto=valor*hora

if salario_bruto<=900:
    imposto_de_renda=0
elif salario_bruto>900 and salario_bruto<=1500:
    imposto_de_renda=salario_bruto*0.05
elif salario_bruto>1500 and salario_bruto<=2500:
    imposto_de_renda=salario_bruto*0.10
elif salario_bruto>2500:
    imposto_de_renda=salario_bruto*0.20
else:
    print("ERRO")
#calculos FGTS e INSS
fgts=salario_bruto*0.11
inss=salario_bruto*0.10

#salario liquido
salario_liquido=salario_bruto-imposto_de_renda-inss
total_descontos=imposto_de_renda+inss

#impressão dos valores

print("==================")
print(f"| SALÁRIO BRUTO: {salario_bruto:.2f}")
print(f"| IMPOSTO DE RENDA: {imposto_de_renda:.2f}")
print(f"| INSS: {inss:.2f}")
print(f"| FGTS: {fgts:.2f}")
print(f"| TOTAL DE DESCONTOS: {total_descontos:.2f}")
print(f"| SALÁRIO LIQUIDO: {salario_liquido:.2f}")
print("==================")
print()
