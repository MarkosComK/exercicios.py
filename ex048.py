#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500
v = 0
s = 0
for c in range(0, 500, 3):
    if c % 2 != 0:
        v += c
        s += 1
print(f'A soma dos {s} números é igual a {v}')