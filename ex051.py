PrimeiroTermo = int(input('Primeiro termo: '))
Razao = int(input('Razão: '))
Decimo = PrimeiroTermo + (11 - 1) * Razao
for c in range(PrimeiroTermo, Decimo, Razao):
    print(f'{c} → ', end=' ')
print('→ ACABOU!')
