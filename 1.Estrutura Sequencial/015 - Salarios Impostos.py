''' Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

horas=int(input("HORAS TRABALHADAS: "))
ganho_hora=float(input("GANHO POR HORA "))
print()

salario_bruto=horas*ganho_hora
imposto_de_renda=salario_bruto*0.11
inss=salario_bruto*0.08
sindicato=salario_bruto*0.05
salario_liquido=salario_bruto-imposto_de_renda-inss-sindicato

print(f"SALÁRIO BRUTO: {salario_bruto}")
print(f"IMPOSTO DE RENDA: {imposto_de_renda}")
print(f"INSS: {inss}")
print(f"SINDICATO: {sindicato}")
print(f"SALÁRIO LÍQUIDO: {salario_liquido}")
