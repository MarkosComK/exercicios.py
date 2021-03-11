lista = 'caderno', 20.00, 'lápis', 01.50, 'lapizeira', 01.00
print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    if pos % 2 == 1:
        print(f'R${lista[pos]:>5}')
print('-'*40)