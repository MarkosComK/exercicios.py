#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada
from time import sleep
def contador(início, fim, passo):
    print('-='*40)
    sleep(0.5)
    print(f'Contando de {início} até {fim} de {passo} em {passo}: ')
    sleep(2.5)
    if passo < 0:
        passo = passo*-1
    if passo == 0:
        passo = 1
    if fim > início:
        cont = início
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += passo
    elif início > fim:
        cont = início
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= passo
    print()


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
início = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(início, fim, passo)
