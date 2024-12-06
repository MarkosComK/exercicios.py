#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.


from random import randint
from time import sleep
#from operator import itemgetter
jogadores = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
sleep(1)
print('Valores sorteados:')
sleep(1)
for k, v in jogadores.items():
    print(f'    O {k} tirou {v}')
    sleep(1.5)
contador = 1
sleep(1)
print('Ranking dos jogadores:')
sleep(1)
for item in sorted(jogadores, key = jogadores.get):
    print (f'    O {contador}º lugar: {item} com  {jogadores[item]}')
    sleep(1)
    contador += 1

# função itemgetter também serve para classificar dicionários por ordem
#jogadores = sorted(jogadores.items(), key=itemgetter(1))
#print(jogadores)