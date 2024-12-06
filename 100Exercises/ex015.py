#Escreva um programa que pergunte a quantidade de Km percorridos por um carro aligado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
v1 = float(input('Quantos km rodados? '))
v2 = float(input('Quandos dias foi alugado? '))
p = (v2 * 60) + (v1 * 0.15)
print(f'O valor a ser pago é de R${p:.2f}')