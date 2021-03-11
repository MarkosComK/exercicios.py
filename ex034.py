salario = float(input('Digite o salário: '))
salario10 = salario / 10
salario15 = (salario / 100) * 15
if salario > 1250:
    print(f'O valor do salário com aumento de 10% será de {salario + salario10:.2f}R$')
if salario <= 1250:
    print(f'O valor do salário com aumento de 15% será de {salario + salario15:.2f}R$')