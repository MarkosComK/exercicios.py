#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
soma = numero = c = 0
numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:
    c += 1
    soma += numero
    numero = int(input('Digite um número [999 para parar]: '))
print(f'A soma dos {c-1} valores digitados é = {soma}')