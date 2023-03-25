
'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo
    grau e o programa não deve fazer pedir os demais valores,
    sendo encerrado;
Se o delta calculado for negativo, a equação não possui raízes reais.
    Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz
    real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais;
    informe-as ao usuário;
'''
# Inputs
a=float(input("Digite o valor de A: "))
b=float(input("Digite o valor de B: "))
c=float(input("Digite o valor de C: "))

# If's e Cálculos
if a==0:
    print("Caso A seja igual a 0, não é uma equação quadrática")
else:
    delta=b**2-4*a*c
    if delta<0:
        print("A equação não possui raizes reais")
    elif delta==0:
        x_1=-b+(delta**0.5)/2*a
        print(f"Para delta=0, há apenas uma raiz real, e neste caso esta corresponde a {x_1}")
    elif delta>0:
        x_1=(-b+delta**0.5)/2*a
        x_2=(-b-delta**0.5)/2*a
        print(f"Há duas raizes reais, sendo estas {x_1:.3f} e {x_2:.3f}")