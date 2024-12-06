#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    opcao = int(input(('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair
    
    >>>>>Qual a sua opção: ''')))
    if opcao == 1:
        print(f'A soma entre {n1:.0f} + {n2:.0f} é {n1+n2:.0f}')
    elif opcao == 2:
        print(f'A multiplicação entre {n1:.0f} x {n2:.0f} é {n1*n2:.0f}')
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1:.0f} é o maior número')
        elif n2 > n1:
            print(f'{n2:.0f} é o maior número')
        elif n1 == n2:
            print(f'{n1:.0f} = {n2:.0f}')
    elif opcao == 4:
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif opcao == 5:
        opcao = 5
    print('-='*20)
    sleep(2)