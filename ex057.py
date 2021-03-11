sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, por favor informe seu sexo: ')).upper().strip()[0]
print(f'Opção {sexo} registrada com sucesso')