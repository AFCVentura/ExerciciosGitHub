# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("TURNO DE ESTUDO:")
print("M - Matutino")
print("V - Vespertino")
print("N - Noturno")
letra=input("Seu turno: ").upper()

if letra=="M":
    print("Bom dia")
elif letra=="V":
    print("Boa tarde")
elif letra=="N":
    print("Boa noite")
else:
    print("Digite um valor válido")