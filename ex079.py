lista = []
while True:
    n = (int(input('Digite um valor: ')))
    if n in lista:
        print('Valor duplicado! Não vou adicionar...')
    if n not in lista:
        lista.append(n)
    o = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if o == 'N':
        break
print('-='*50)
lista.sort()
print(f'Você digitou os valores {lista}')