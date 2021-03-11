viajem = float(input('Qual é a distância da sua viajem? '))
print(f'Você está prestes a começar uma viajem de {viajem} KM')
if viajem < 200:
    preco = viajem * 0.5
else:
    preco = viajem * 0.45
print(f'O valor da sua passagem é de {preco:.2f}R$')