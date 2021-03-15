#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def área(largura, comprimento):
    return l * c


l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
print(f'A área de um terreno de {l} X {c} é de {área(l, c)}m²')