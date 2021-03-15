#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
n4 = int(input('Digite o 4º número: '))
tupla = (n1, n2, n3, n4)
c = c2 = 0
for i in tupla:
    if i == 9:
        c += 1
for i in tupla:
    if i != 3:
        c2 += 1
    if i == 3:
        break
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 aparece {c} vezes') #função count() pode  ser usada para facilitar
print(f'O valor 3 aparece na posição {c2+1}') #função index() pode ser usada para facilitar
print(f'Os valores pares digitados foram ', end=' ')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')