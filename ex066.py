soma = contador = 0
while True:
    valor = int(input('Digite um valor [999 para parar]: '))
    if valor == 999:
        break
    soma += valor
    contador += 1
print(f'A soma dos {contador} valores foi {soma}')