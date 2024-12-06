#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input('Qual a velocidade atual do veículo? '))
multa = (velocidade - 80) * 7 #Cálcula o valor da multa
if velocidade > 80:
    print(f'Você foi MULTADO, o valor total de sua multa é de {multa:.2f}R$')
else:
    print('Sua velocidade está dentro do limite máximo permitido.')
print('Tenha um bom dia, diriga com segurança!')