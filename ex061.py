PrimeiroTermo = int(input('Primeiro termo: '))
Razao = int(input('Razão: '))
Decimo = PrimeiroTermo + (11 - 1) * Razao
c = 0
while c < 10:
    print(f'{PrimeiroTermo} → ', end='')
    PrimeiroTermo += Razao
    c += 1
print('ACABOU!')