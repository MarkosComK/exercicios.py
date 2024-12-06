def ficha(n='<desconhecido>', gols=0):
    return print(f'O jogador {n} fez {gols} gol(s) no campeonato')


nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome == '':
    ficha(gols=gols)
elif gols == '':
    ficha(nome)
elif nome == '' and gols == '':
    ficha()
else:
    ficha(nome, gols)