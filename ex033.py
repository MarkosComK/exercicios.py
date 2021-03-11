valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
valor3 = int(input('Digite mais um valor: '))
menor = valor2
if valor1 < valor2 and valor1 < valor3:
    menor = valor1
if valor3 < valor2 and valor3 < valor1:
    menor = valor3
print(f'O menor valor digitado foi {menor}')
maior = valor2
if valor1 > valor2 and valor1 > valor3:
    maior = valor1
if valor3 > valor2 and valor3 > valor1:
    maior = valor3
print(f'O maior valor digitado foi {maior}')