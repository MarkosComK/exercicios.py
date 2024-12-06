#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
nome = str(input('Digite seu nome completo: ')).strip().split()
UltimoNome = nome[len(nome)-1]
print(UltimoNome)
print(f'Muito prazer {nome}')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {UltimoNome}')
