#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
#Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
numero = int(input('Quantos termos da sequencia você quer mostrar: '))
t1 = 0
t2 = 1
tf = 0
nt = 0
while tf != numero:
    nt = t1 + t2
    print(f'{nt} → ', end='')
    t1 = t2
    t2 = nt
    tf += 1
print('FIM')