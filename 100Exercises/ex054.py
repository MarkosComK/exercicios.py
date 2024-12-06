#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
Ano = date.today().year
contador1 = 0
contador2 = 0
for c in range(1, 8):
    p = int(input(f'Em que ano a {c}º pessoa nasceu: '))
    if p > Ano - 18:
        contador1 += 1 #pessoas menores de idade
    else:
        contador2 += 1 #pessoas maiores de idade
print(f'Temos {contador2} pessoas maiores de 18 anos')
print(f'Temos {contador1} pessoas menores de 18 anos')