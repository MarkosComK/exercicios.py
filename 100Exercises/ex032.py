# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import datetime

ano = int(input('Que ano você quer analisar? coloque 0 para análisar o ano atual: '))
if ano == 0: 
    ano = datetime.now().year
if ano % 4 == 0:
    if ano % 100 != 0:
        print(f'O ano {ano} foi bissexto e fevereiro teve 29 dias.')
print(f'O ano {ano} não é bissexto.')