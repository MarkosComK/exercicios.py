lista = []
#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média
dados = {
    'nome': ' ',
    'sexo': ' ',
    'idade': ' '
}
soma = 0
while True:
    nome = str(input('Nome: '))
    sexo = str(input('Sexo[M/F]'))[0]
    while sexo not in 'FfMm':
        sexo = str(input('ERRO: Por favor, digite apenas M ou F: '))
    idade = int(input('Idade: '))
    dados['nome'] = nome
    dados['sexo'] = sexo
    dados['idade'] = idade
    lista.append(dados.copy())
    soma += idade
    del dados['nome'], dados['sexo'], dados['idade']
    o = str(input('Quer continuar[S/N]? '))[0]
    while o not in 'SsNn':
        o = str(input('ERRO: Responda apenas S ou N: '))
    if o in 'Nn':
        break
media = soma / len(lista)
print(f'O grupo tem {len(lista)} pessoas')
print(f'A média de idade é de {media} anos')
print('As mulheres cadastradas foram: ', end='')
for s in range(0, len(lista)):
    if lista[s]['sexo'] in 'Ff':
        print(lista[s]["nome"], end=' ')
print()
print('Lista das pessoas que estão acima da média')
for i in range(0, len(lista)):
    if lista[i]['idade'] > media:
        print(f'nome = {lista[i]["nome"]}; sexo = {lista[i]["sexo"]}; idade = {lista[i]["idade"]}')