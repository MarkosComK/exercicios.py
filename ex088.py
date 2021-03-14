from random import randint
from time import sleep
print('-'*40)
print('            JOGO DA MEGA SENA')
print('-'*40)
palpites = int(input('Quantos jogos você quer sortear? '))
stop = 0
print('>' * 4, f'SORTEANDO {palpites} JOGOS', '<' * 4)
sleep(1.5)
while stop < palpites:
    lista = []
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    print(f'Jogo {stop+1}: {lista}')
    sleep(0.5)
    stop += 1