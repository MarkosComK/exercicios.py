nome = str(input('Digite seu nome: '))
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: ', nome.upper())
print('Seu nome em minúsculas é: ', nome.lower())
nome2 = len(nome.replace(' ', ''))
FirstName = nome.split()
print(f'Seu nome tem ao todo {nome2} letras')
print(f'Seu primeiro nome é {FirstName[0]} e tem {len(FirstName[0])} letras')

