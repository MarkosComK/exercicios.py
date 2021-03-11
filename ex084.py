dados = []
pessoas = []
maiorp = menorp = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if pessoas[1] >= maiorp:
        maiorp = pessoas[1]
    if pessoas[1] <= menorp:
        menorp = pessoas[1]
    if len(dados) == 0:
        maiorp = menorp = pessoas[1]
    o = str(input('Quer continuar[S/N]? ')).upper().strip()[0]
    dados.append(pessoas[:])
    pessoas.clear()
    if o == 'N':
        break
print(f'Um total de {len(dados)} pessoas foram cadastradas')
print(f'As pessoas mais pesadas tem {maiorp} KG, ', end='')
for p in dados:
    if p[1] == maiorp:
        print(f'{p[0]}, ', end='')
print()
print(f'As pessoas mais leves tem {menorp} KG, ', end='')
for p in dados:
    if p[1] == menorp:
        print(f'{p[0]}, ', end='')