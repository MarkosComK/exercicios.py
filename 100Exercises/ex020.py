#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import sample
lista = []
v = 1
for c in range(0,4):
    n = input(f'Digite o nome da {v}º pessoa: ')
    v = v + 1
    lista.append(n)
print('A ordem de apresentação será: ')
print(sample(lista, len(lista)))