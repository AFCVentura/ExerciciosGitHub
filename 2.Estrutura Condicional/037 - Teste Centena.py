'''Exercicio 037
Faça um Programa que leia um número inteiro maior que 0 e menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo: 326 = 3 centenas, 2 dezenas e 6 unidades 12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''

# Input
numero=int(input("Digite um número inteiro de 1 até 999: "))

# IF's
if numero>0 and numero<1000:
    if numero>=100:
        centena=numero//100
        if numero>=10:
            dezena=(numero-(centena*100))//10
            unidade=numero-(centena*100)-(dezena*10)
        else:
            dezena=0
            unidade=numero-(centena*100)-(dezena*10)
    else:
        centena=0
        if numero>=10:
            dezena=(numero-(centena*100))//10
            unidade=numero-(centena*100)-(dezena*10)
        else:
            dezena=0
            unidade=numero-(centena*100)-(dezena*10)


# Impressão
print("=====================================================")
print(f"O número {numero} possui {centena} centenas, {dezena} dezenas e {unidade} unidades")
print("=====================================================")
#Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

