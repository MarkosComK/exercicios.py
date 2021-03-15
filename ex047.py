#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
escolha = int(input('Escolha um número e mostrarei todos os números pares até chegar nele: '))
for c in range(0, escolha+2, 2):
    print(c, end=' ')
