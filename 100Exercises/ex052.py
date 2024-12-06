#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
Numero = int(input('Digite um número: '))
Contador = 0
for c in range(Numero, 0, -1):
    if Numero % c == 0:
        print(f'\033[31m|{c}|', end=' ')
        Contador += 1
    else:
        print(f'\033[32m{c}', end=' ')
print('\033[m')
print(f'O número {Numero} foi dívisivel {Contador} vezes')
if Contador > 2:
    print('E por isso ele NÃO É PRIMO!')
elif Contador <= 2:
    print('E por isso ele É PRIMO!')
