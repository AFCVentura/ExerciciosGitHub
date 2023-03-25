# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

horas=float(input("HORAS TRABALHADAS NO MÊS: "))
ganho_hora=float(input("GANHO POR HORA: "))
print()

salario=horas*ganho_hora

print(f"SALÁRIO: {salario}")