'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:    
    tipo de carne
    quantidade de carne
    preço total
    tipo de pagamento
    valor do desconto
    valor a pagar..'''

# Mostrar valor do desconto

# Cabeçalho
print("======================================================")
print("       H I P E R M E R C A D O   T A B A J A R A      ")
print("======================================================")
print()

print("//////////////////////////////////////////////////////")
print("                    P R O M O Ç Ã O                   ")
print("//////////////////////////////////////////////////////")
print()

# Tabela de Preços
print("======================================================")
print("                    TABELA DE PREÇOS                  ")
print("======================================================")
print("                   Até 5 Kg              Acima de 5 Kg")
print("File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg")
print("Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg")
print("Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg")
print("======================================================")
print("    Compras no Cartão Tabajara dão 5% de desconto     ")
print("======================================================")
print()

# Inputs
print("======================================================")
print("Você pode escolher apenas uma das carnes para participar")
print("------------------------------------------------------")
carne=input("Carne escolhida: ").upper()
print("------------------------------------------------------")
print("         Compras de até 5KG têm custo reduzido        ")
print("------------------------------------------------------")
peso=int(input("Peso da carne escolhida: KG "))
print("------------------------------------------------------")
print("       Escolha entre dinheiro ou Cartão Tabajara      ")
print("------------------------------------------------------")
pagamento=input("Forma de Pagamento: ").upper()
print("======================================================")
print()

# IF's Carnes
if carne=="FILE DUPLO":
    if peso<=5:
        valor_total=4.90*peso
        valor_desconto=(5.8-4.9)*peso
    else:
        valor_total=5.80*peso
        valor_desconto=0
elif carne=="ALCATRA":
    if peso<=5:
        valor_total=5.90*peso
        valor_desconto=(6.8-5.9)*peso
    else:
        valor_total=6.80*peso
        valor_desconto=0
elif carne=="PICANHA":
    if peso<=5:
        valor_total=6.90*peso
        valor_desconto=(7.8-6.9)*peso
    else:
        valor_total=7.80*peso
        valor_desconto=0
else:
    print("ERRO")

# IF Desconto e valor final
if pagamento=="CARTÃO" or pagamento=="CARTÃO TABAJARA" or pagamento=="CARTAO" or pagamento=="CARTAO TABAJARA":
    valor_desconto+=(valor_total*0.05)
valor_final=valor_total-valor_desconto

# Impressão
print("======================================================")
print(f"Carne: {carne}")
print(f"Peso: {peso:.3f} KG")
print(f"Preço Bruto: R${valor_total:.2f}")
print(f"Forma de Pagamento: {pagamento}")
print(f"Valor do Desconto: R${valor_desconto:.2f}")
print(f"Preço Final: R${valor_final:.2f}")
print("======================================================")