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