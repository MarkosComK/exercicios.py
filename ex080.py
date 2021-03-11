lista = []
for c in range(5):
    numero = int(input("Digite um número: "))
    for pos, item in enumerate(lista):
        if numero < item:
            lista.insert(pos, numero)
            print(f'Adicionado na posiçao {pos}')
            break
    else:
        print(f'Adicionado ao final da lista...')
        lista.append(numero)
print("Lista atual:", lista)