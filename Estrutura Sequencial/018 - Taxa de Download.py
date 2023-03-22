#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho=float(input("DIGITE O TAMANHO DO DOWNLOAD EM MB: "))
velocidade_segundo=float(input("DIGITE A VELOCIDADE DA INTERNET EM MBPS: "))

velocidade_minuto=velocidade_segundo*60
tempo_minuto=tamanho//velocidade_minuto
tempo_segundo=tamanho/velocidade_segundo
tempo_final_segundo=tempo_segundo-(tempo_minuto*60)
print(f"A velocidade de download é de {tempo_minuto:.0f} minuto(s) e {tempo_final_segundo:.0f} segundo(s)")