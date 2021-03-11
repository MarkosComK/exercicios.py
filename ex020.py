from random import sample
lista = []
v = 1
for c in range(0,4):
    n = input(f'Digite o nome da {v}º pessoa: ')
    v = v + 1
    lista.append(n)
print('A ordem de apresentação será: ')
print(sample(lista, len(lista)))