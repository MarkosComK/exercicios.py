#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
lista = []
for c in range(1, 6):
    lista.append(int(input(f'Digite o {c}º valor: ')))
print(f'Você digitou os valores {lista}')
print(f'O maior valor da lista foi {max(lista)} nas posições', end=' ')
for p, n in enumerate(lista):
    if n == max(lista):
        print(f'{p+1} ', end='')
print()
print(f'O menor valor da lista foi {min(lista)} nas posições', end=' ')
for p, n in enumerate(lista):
    if n == min(lista):
        print(f'{p+1} ', end='')