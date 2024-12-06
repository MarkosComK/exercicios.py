#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
PrimeiroTermo = int(input('Primeiro termo: '))
Razao = int(input('Razão: '))
Decimo = PrimeiroTermo + (11 - 1) * Razao
c = 0
t = 10
total = 0
mais = 10
while t != 0:
    total += mais
    while c < total:
        print(f'{PrimeiroTermo} → ', end='')
        PrimeiroTermo += Razao
        c += 1
    print('PAUSA')
    print()
    t = int(input('Quantos termos a mais você quer mostrar?'))
    print()
print('FIM!')