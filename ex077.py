lista = 'APRENDER', 'VERIFICAR', 'FAZER', 'USAR', 'SER', 'ATRIBUIR'
vogais = 'a' 'e' 'i' 'o' 'u'
for p in lista:
    print(f'Na palavra {p} temos', end=' ')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end=' ')
    print()