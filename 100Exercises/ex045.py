#Crie um programa que faça o computador jogar Jokenpô com você.
import sys
from random import randint
from time import sleep
print('===========JOKENPO===========')
print('''Suas opções:
[ 0 ]PEDRA
[ 1 ]PAPEL
[ 2 ]TESOURA''')
itens = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input('Qual é sua jogada: '))
if jogador > 2:
    print('OPÇÃO INVÁLIDA')
    sys.exit()
pc = randint(0, 2)
sleep(1)
print('       JO')
sleep(1)
print('       KEN')
sleep(1)
print('       PO')
sleep(1)
print('-='*19)
print(f'O computador escolheu {itens[pc]}')
print(f'O jogador escolheu {itens[jogador]}')
print('-='*19)
if jogador - pc == 1:
    print('O jogador venceu a máquina!')
elif jogador - pc == 0:
    print('EMPATE!')
else:
    print('A máquina venceu!')