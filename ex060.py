c = numero = int(input('Número: '))
f = 1
print(f'Calculando o fatorial de {numero}')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)