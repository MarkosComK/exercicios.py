print('-'*37)
print('             Santos Bank')
print('-'*37)
valor = int(input('Qual valor você quer sacar: R$'))
ced = 50
ced20 = 20
ced10 = 10
ced1 = 1
contced50 = contced1 = contced10 = contced20 = 0
while True:
    if valor >= ced:
        valor -= ced
        contced50 += 1
    if valor >= 20 and valor < ced:
        valor -= ced20
        contced20 += 1
    if valor >= 10 and valor < ced20:
        valor -= ced10
        contced10 += 1
    if valor >= 1 and valor < ced10:
        valor -= ced1
        contced1 += 1
    if valor <= 0:
        break
print('Você receberá')
print(f'     {contced50} notas de 50R$')
print(f'     {contced20} notas de 20R$')
print(f'     {contced10} notas de 10R$')
print(f'     {contced1} notas de 1R$')
print('Obrigado. Volte sempre!')