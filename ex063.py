numero = int(input('Quantos termos da sequencia você quer mostrar: '))
t1 = 0
t2 = 1
tf = 0
nt = 0
while tf != numero:
    nt = t1 + t2
    print(f'{nt} → ', end='')
    t1 = t2
    t2 = nt
    tf += 1
print('FIM')