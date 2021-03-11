lista = []
while True:
    v = int(input('Digite um valor: '))
    lista.append(v)
    o = str(input('Deseja continuar [S/N]? '))[0].upper().strip()
    if o == 'N':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado dentro da lista')