# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
from random import randint
cont = pc = valor = 0
while True:
    pc = randint(0, 10)
    valor = int(input('Digite um valor: '))
    opcao = ' '
    soma = valor + pc
    while opcao not in 'pi':
        opcao = str(input('Par ou ímpar:'))[0].lower()
    if soma % 2 == 0 and opcao in 'p':
        cont += 1
        print(f'Você jogou {valor} e o computador jogou {pc}. Total de {soma}: Par. Você venceu!')
    elif soma % 2 != 0 and opcao in 'i':
        print(f'Você jogou {valor} e o computador jogou {pc}. Total de {soma}: Ímpar. Você venceu!')
        cont += 1
    else:
        print(f'você jogou {valor} e o computador {pc}. Total de {soma} você perdeu')
        print(f'Você conseguiu {cont} vitórias contra a máquina. Parabéns. Volte sempre!')
        break
    