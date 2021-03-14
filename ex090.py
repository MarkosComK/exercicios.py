dicionario = {'nome': ' ', 'media':' ', 'situação': ' '}
nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))
if media >= 7:
    dicionario['situação'] = 'Aprovado'
elif media >= 5 and media < 7:
    dicionario['situação'] = 'Recuperação'
elif media < 5:
    dicionario['situação'] = 'Reprovado'
dicionario['nome'] = nome
dicionario['media'] = media
for k, v in dicionario.items():
    print(f'     - {k} é igual a {v}')
