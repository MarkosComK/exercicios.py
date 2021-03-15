#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
PrimeiroTermo = int(input('Primeiro termo: '))
Razao = int(input('Razão: '))
Decimo = PrimeiroTermo + (11 - 1) * Razao
for c in range(PrimeiroTermo, Decimo, Razao):
    print(f'{c} → ', end=' ')
print('→ ACABOU!')
