#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) /2
    lista.append([nome, [nota1, nota2], media])
    o = str(input('Quer continuar[S/N]? '))[0]
    if o in 'Nn':
        break
print(f'{"No.":<5} {"Nome":^10} {"Média":>5}')
print('-'*50)
for i, v in enumerate(lista):
    print(f'{i:<5} {v[0]:^10} {v[2]:>5}')
print('-'*50)
while True:
    op = int(input('Mostrar as notas de qual aluno[999 interrompe]? '))
    if op == 999:
        break
    elif op <= len(lista)-1:
        print(f'As notas de {lista[op][0]} são {lista[op][1]}')
    elif op > len(lista)-1:
        print('Aluno não cadastrado. Tente novamente.')
        op = int(input('Mostrar as notas de qual aluno[999 interrompe]? '))