from time import sleep
from random import randint

print('-='*30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-='*30)
numero = randint(0, 5) # Faz o computador 'pensar' em um número
chute = int(input('Em que número eu pensei? ')) #Pede a resposta do jogador
print('PROCESSANDO...')
sleep(3)
if chute == numero:
    print(f'Você acertou! eu pensei no número {numero}')
else:
    print(f'Você errou! O número que pensei foi o {numero}')
print('Fim do programa')