#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 
from time import sleep
while True:
    sleep(1)
    numero = int(input('Quer ver a tabuada de qual valor: '))
    if numero < 0:
        print('Programa encerrado, volte sempre!')
        break
    c = 1
    print('-='*6)
    sleep(1)
    while c < 11:
        print(f'{numero} x {c} = {numero * c}')
        c += 1
    print('-='*6)