dados = {
    'nome': ' ',
    'gol': ' ',
    'total': ' '
}
gol = []
nome = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {nome} jogou? '))
total = 0
for c in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {c}? '))
    gol.append(gols)
    total += gols
dados['nome'] = nome
dados['gol'] = gol
dados['total'] = total
print('-='*50)
print(dados)
print('-='*50)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*50)
print(f'O jogador {nome} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f' Na partida {c}, fez {dados["gol"][c]} gols')
print(f'Foi um total de {total} gols')