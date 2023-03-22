'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante :
    aumento de 5% Após o aumento ser realizado,
informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
'''

salario_base=float(input("DIGITE O SALÁRIO INICIAL DO FUNCIONÁRIO: "))

if salario_base<=280:
    decimal=0.2
    salario_final=salario_base+(salario_base*decimal)
elif salario_base<=700:
    decimal=0.15
    salario_final=salario_base+(salario_base*decimal)
elif salario_base<1500:
    decimal=0.10
    salario_final=salario_base+(salario_base*decimal)
elif salario_base>=1500:
    decimal=0.05
    salario_final=salario_base+(salario_base*decimal)
else:
    print("Erro")

print(f"==============")
print(f"Salário anterior ao reajuste: R${salario_base:.2f}")
print(f"Percentual de aumento aplicado: {decimal*100}%")
print(f"Valor do reajuste: R${salario_base*decimal:.2f}")
print(f"Salário Reajustado: R${salario_final:.2f}")
print(f"==============")
