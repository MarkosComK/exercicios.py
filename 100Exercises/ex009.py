#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
n = float(input('Digite um número para ver sua tabuada: '))
v = 1
print('-' * 10)

for c in range(0,9):
    v += 1
    print(f'{n:.0f} x {v:2} = {n*v:.0f}')
 
print('-' * 10)
