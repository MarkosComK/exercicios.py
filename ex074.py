from random import randint
tupla = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print('Os valores sorteados foram ', end='')
for n in tupla:
    print(f'{n} ', end='')
print()
sorted(tupla)
tupla2 = sorted(tupla)
menor = tupla2[0]
maior = tupla2[4]
print(f'O menor valor sorteado foi {menor}') #comando "MAX" pode ser usado para facilitar
print(f'O maior valor sorteado foi {maior}') #comando "MIN" pode ser usado para facilitar