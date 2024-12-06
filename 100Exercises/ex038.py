#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais
v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo valor: '))
if v1 > v2:
    print('O PRIMEIRO valor é maior.')
elif v2 > v1:
    print('O SEGUNDO valor é maior')
elif v1 == v2:
    print('Os dois valores são IGUAIS')