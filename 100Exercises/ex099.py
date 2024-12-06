#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep
def maior(*num):
    maior = 0
    sleep(0.5)
    print('Analisando os valores')
    for valor in num:
        print(valor, end=' ', flush=True)
        sleep(0.5)
        if valor > maior:
            maior = valor
    print()
    sleep(0.5)
    print(f'Foram informados {len(num)} valores')
    sleep(0.5)
    print(f'O maior valor foi o {maior}')
    sleep(0.5)
    print('-='*10)
    sleep(0.5)




maior(1, 8, 2, 4, 5, 5, 9)
maior(2, 1, 3)
maior(-1, 5, 3, 4)
maior()