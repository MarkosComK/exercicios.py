#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
lista = 'APRENDER', 'VERIFICAR', 'FAZER', 'USAR', 'SER', 'ATRIBUIR'
vogais = 'a' 'e' 'i' 'o' 'u'
for p in lista:
    print(f'Na palavra {p} temos', end=' ')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end=' ')
    print()