v1 = float(input('Quantos km rodados? '))
v2 = float(input('Quandos dias foi alugado? '))
p = (v2 * 60) + (v1 * 0.15)
print(f'O valor a ser pago é de R${p:.2f}')