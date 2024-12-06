#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira
from math import trunc
n = float(input('Digite um valor: '))
print(f'O valor digitado foi {n} e sua porção inteira é {trunc(n)}')
