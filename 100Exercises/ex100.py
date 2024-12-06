#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
def sortear(a):
    print('Sorteando 5 valores da lista: ', end=' ', flush=True)
    for c in range(0, 5):
        n = randint(0, 10)
        c = c
        a.append(n)
        sleep(0.5)
        print(f'{n}', end=' ', flush=True)
        sleep(0.5)
    print()

def somaPar(a):
    somaPar = 0
    for valor in a:
        if valor % 2 == 0:
            somaPar += valor
    return somaPar


a = []
sortear(a)
sleep(0.5)
print(f'Somando os valores pares de {a} temos: {somaPar(a)}')