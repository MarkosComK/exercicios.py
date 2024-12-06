#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

lista = []
dados = {
    'nome': ' ',
    'gol': ' ',
    'total': ' '
}
gol = []
while True:
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
    lista.append(dados.copy())
    del dados['nome'], dados['gol'], dados['total']
    o = str(input('Quer continuar? [S/N] '))
    while o not in 'SsNn':
        o = str(input('ERRO: Digite apenas S ou N. '))
    if o in 'Nn':
        break
print('-='*50)
print(f'{"cod"} {"nome":<5} {"gol":^15} {"total":>8}')
print('-='*50)
print(lista)
for c in range(0, len(lista)):
    print(f'{c}   {lista[c]["nome"]:<5}      {lista[c]["gol"]}       {lista[c]["total"]}')
print('-='*50)