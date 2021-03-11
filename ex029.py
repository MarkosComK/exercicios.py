velocidade = int(input('Qual a velocidade atual do veículo? '))
multa = (velocidade - 80) * 7 #Cálcula o valor da multa
if velocidade > 80:
    print(f'Você foi MULTADO, o valor total de sua multa é de {multa:.2f}R$')
else:
    print('Sua velocidade está dentro do limite máximo permitido.')
print('Tenha um bom dia, diriga com segurança!')