# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida
peso = float(input('Qual o seu peso: '))
altura = float(input('Qual a sua altura: '))
imc = peso / (altura*altura)
print(f'Seu imc é de {imc:.2f}')
if imc < 18:
    print('Você está abaixo do peso!')
elif 24.9 > imc > 18:
    print('Você está no peso ideal!')
elif 30 > imc > 24.9:
    print('Você está com sobrepeso!')
elif imc > 30:
    print('Você está com obesidade!')