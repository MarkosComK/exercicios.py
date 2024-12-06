# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
s = 0 #Variável que recebe os valores digitadoes se forem PAR
cont = 0 # contador de números pares
for c in range(1, 7):
    n = int(input(f'Digite o {c} número, se for par será somado: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'Você informou {cont} número(s) pares e a soma deles foi {s}')