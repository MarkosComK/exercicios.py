#Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la. sabendo que cada litro de tinta, pinta uma área de 2m².
l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
A = l * a 
#1 litro de tinta pinta 2m²
print(f'Sua parede tem a dimensão de {l} x {a} e sua área é de {A}')
print(f'Para pintar a parede você precisará de {A/2}l de tinta.')