from random import randint
print('''Sou seu computador e vou pensar em um número entre 0 e 10. 
Tende advinhar...''')
Computador = randint(0, 10)
contador = 0
acertou = False
while not acertou:
    contador += 1
    palpite = int(input('Digite seu palpite: '))
    if palpite == Computador:
        acertou = True
    if palpite < Computador:
        print('Mais... Tente novamente: ')
    elif palpite > Computador:
        print('Menos... Tente novamente: ')
print(f'Acertou com {contador} tentativas. Parabéns!')