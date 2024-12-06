#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = []
listaPar = []
listaImpar = []
while True:
    n = int(input('Digite um valor: '))
    o = str(input('Quer continuar? [S/N]? '))[0].upper().strip()
    lista.append(n)
    if o == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        listaPar.append(v)
    else:
        listaImpar.append(v)
print(f'A lista com todos os valores é {lista}')
print(f'Os números pares digitados foram {listaPar}')
print(f'Os números ímpares digitados foram {listaImpar}')