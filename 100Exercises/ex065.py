#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
total = 0
soma = 0
maior = 0
menor = 0
while True:
    n = float(input('Digite um número: '))
    total += 1
    soma += n
    menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    c = str(input('Quer continuar[S/N]: '))[0].upper()
    if c == 'N':
        break
    if c not in 'NS':
        print('OPÇÃO INVÁLIDA')
        break
media = soma / total
print(f'A soma dos valores digitados é = {soma:.0f}')
print(f'A média dos valores digitados é = {media:.2f}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')