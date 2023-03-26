# Faça um programa que leia e valide as seguintes informações: Nome: maior que 3 caracteres; Idade: entre 0 e 150; Salário: maior que zero; Sexo: 'f' ou 'm'; Estado Civil: 's', 'c', 'v', 'd';

# Inputs
nome=input("Digite seu nome: ")
while len(nome)<3:
    nome=input("Digite um nome válido:")
print()

idade=int(input("Digite sua idade: "))
while idade<=0 or idade>=150:
    idade=int(input("Digite uma idade válida: "))
print()

salario=float(input("Digite seu salário: R$"))
while salario<=0:
    salario=float(input("Digite um salário válido: R$"))
print()

genero=input("Digite seu gênero [m, f, o]: ").upper()
while genero!="F" and genero!="M" and genero!="O":
    genero=input("Digite um gênero válido: ").upper()
print()

estado_civil=input("Digite seu estado civil [s, c, v, d]: ").upper()
while estado_civil!="S" and estado_civil!="C" and estado_civil!="V" and estado_civil!="D":
    estado_civil=input("Digite um estado civil válido: ").upper()
print()


# IF's de Impressão
if genero=="F":
    genero="Feminino"
elif genero=="M":
    genero="Masculino"
elif genero=="O":
    genero="Outros"

if estado_civil=="S":
    estado_civil="Solteiro"
elif estado_civil=="C":
    estado_civil="Casado"
elif estado_civil=="V":
    estado_civil="Viúvo"
elif estado_civil=="D":
    estado_civil="Divorciado"


# Impressão
print("==========================")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")
print(f"Gênero: {genero}")
print(f"Estado Civil: {estado_civil}")
print("==========================")