s = float(input('Qual é o salário do Funcionário? R$'))
sca = s + (s / 100 * 15)
print(f'Um funcionário que ganhava R${s},\ncom aumento de 15% passa a receber R${sca:.2f}')