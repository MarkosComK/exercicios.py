#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
PrimeiroTermo = int(input('Primeiro termo: '))
Razao = int(input('Razão: '))
Decimo = PrimeiroTermo + (11 - 1) * Razao
c = 0
while c < 10:
    print(f'{PrimeiroTermo} → ', end='')
    PrimeiroTermo += Razao
    c += 1
print('ACABOU!')