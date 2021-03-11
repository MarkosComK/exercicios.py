casa = int(input('Qual o valor da casa: '))
salario = int(input('Qual o seu salário: '))
anos = int(input('Em quantos anos você deseja pagar: '))
mensal = casa / (anos * 12)
print(f'Para pagar uma casa de {casa}')
print(f'O valor da parcela será de {mensal:.2f}R$')
if salario / 100 * 30 < mensal:
    print('Empréstimo NEGADO')
elif salario / 100 * 30 > mensal:
    print('Empréstimo CONCEDIDO')