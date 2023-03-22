#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: 
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; A mensagem "Reprovado", se a média for menor do que sete; 
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

nome=input("DIGITE O NOME DO ALUNO: ")
nota1=float(input("DIGITE A PRIMEIRA NOTA: "))
nota2=float(input("DIGITE A SEGUNDA NOTA: "))

media=(nota1+nota2)/2
def impressao(S,M):
    print()
    print("=====================")
    print(f"MÉDIA DO ALUNO: {M}")
    print(f"STATUS DO ALUNO: {S}")
    print("=====================")
    

if media>=10:
    status="APROVADO COM DISTINÇÃO"
    impressao(status,media)
elif media>=7:
    status="APROVADO"
    impressao(status,media)
elif media>=0:
    status="REPROVADO"
    impressao(status,media)
else:
    print("Digite um valor válido")