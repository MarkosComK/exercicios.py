#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
lista = []
n = 1
for c in range(0,4):
    v = input(f'Digite o nome do {n} º aluno: ')
    n = n + 1
    lista.append(v)
print(f'O aluno escolhido foi {choice(lista)}')
