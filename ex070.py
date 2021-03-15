#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato. 
print('-'*37)
print('      LOJA SUPER BARATÃO')
print('-'*37)
TotalGasto = ProdutoCaro = cont = MaisBarato = 0
NomeBarato = ' '
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    TotalGasto += preco
    if cont == 0:
        MaisBarato = preco
        NomeBarato = nome
    cont += 1
    if preco < MaisBarato:
        MaisBarato = preco
        NomeBarato = nome
    if preco > 1000:
        ProdutoCaro += 1
    c = str(input('Quer continuar[S/N]'))[0].upper()
    while c not in 'SN':
        c = str(input('Quer continuar[S/N]'))[0].upper()
    if c == 'N':
        break
print(f'O total gasto foi de {TotalGasto:.2f}R$')
print(f'{ProdutoCaro} Produtos custaram mais de 1000R$')
print(f'O produto mais barato foi {NomeBarato} que custa {MaisBarato:.2f}R$')
