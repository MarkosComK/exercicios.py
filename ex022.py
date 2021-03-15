#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome: '))
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: ', nome.upper())
print('Seu nome em minúsculas é: ', nome.lower())
nome2 = len(nome.replace(' ', ''))
FirstName = nome.split()
print(f'Seu nome tem ao todo {nome2} letras')
print(f'Seu primeiro nome é {FirstName[0]} e tem {len(FirstName[0])} letras')

