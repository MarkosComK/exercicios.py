#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
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