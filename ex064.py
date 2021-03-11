soma = numero = c = 0
numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:
    c += 1
    soma += numero
    numero = int(input('Digite um número [999 para parar]: '))
print(f'A soma dos {c-1} valores digitados é = {soma}')