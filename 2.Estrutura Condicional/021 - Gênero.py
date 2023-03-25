# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

print("DIGITE SEU GÊNERO")
print("M: Masculino")
print("F: Feminino")
print("O: Outros")
print("N: Não Especificar")
letra=input("SEU GÊNERO: ")

if letra=="F" or letra=="f":
    genero="Feminino"
    print(f"GÊNERO: {genero}")
if letra=="M" or letra=="m":
    genero="Masculino"
    print(f"GÊNERO: {genero}")
if letra=="O" or letra=="o":
    genero="Outros"
    print(f"GÊNERO: {genero}")
if letra=="N" or letra=="n":
    genero="Não Especificado"
    print(f"GÊNERO: {genero}")