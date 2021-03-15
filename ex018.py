#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians, ceil
a = float(input('Digite o ângulo que você deseja: ')) #ângulo lido em gráus
seno = sin(radians(a))     # os angulo precisa estar em radiano poratanto a função "radians" serve para converter
coseno = cos(radians(a))
tangente = tan(radians(a))
print(f'O seno de {a} é {seno:.2f}')
print(f'O coseno de {a} é {coseno:.2f}')
print(f'A tangente de {a} é {tangente:.2f}')