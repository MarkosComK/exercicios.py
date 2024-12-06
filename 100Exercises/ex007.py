#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
n1 = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))
m = (n1 + n2) / 2  #lembrar dos parenteses para auferir prioridade à soma
print(f'A média entre {n1} e {n2} vale {m:.1f}')