#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
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