from random import choice
lista = []
n = 1
for c in range(0,4):
    v = input(f'Digite o nome do {n} º aluno: ')
    n = n + 1
    lista.append(v)
print(f'O aluno escolhido foi {choice(lista)}')
