#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
MaiorPeso = 0
MenorPeso = 0
for c in range(1, 6):
    Peso = float(input(f'Digite o peso da {c} pessoa em kilos: '))
    if c == 1:
        MaiorPeso = Peso
        MenorPeso = Peso
    if Peso > MaiorPeso:
        MaiorPeso = Peso
    if Peso < MenorPeso:
        MenorPeso = Peso
print(f'A pessoa mais pesada tem {MaiorPeso} Kilos')
print(f'A pessoa mais leve tem {MenorPeso} Kilos')