# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7

genero=input("GÊNERO [M/F]: ")
altura=float(input("ALTURA: "))
print()

if genero=="M" or genero=="m":
    peso_homem=(altura*72.7)-58
    print(f"PESO IDEAL HOMEM: {peso_homem:.1f}")
elif genero=="F" or genero=="f":
    peso_mulher=(altura*62.1)-44.7
    print(f"PESO IDEAL MULHER: {peso_mulher:.1f}")
