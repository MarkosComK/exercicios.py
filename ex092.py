#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
dados = {
    'nome': ' ',
    'idade': ' ',
    'ctps': ' ',
    'contratação': ' ',
    'salário': ' ',
    'aposentadoria': ' '
}
nome = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
ctps = int(input('Carteira de trabalho(0 não tem): '))
if ctps == 0:
    del dados['contratação'], dados['salário'], dados['aposentadoria'], dados['ctps']
if ctps > 0:
    contrato = int(input('Ano de contratação: '))
    salario = float(input('Salário: R$ '))
    aposentadoria = contrato + 35 - nascimento
ano = date.today().year
idade = ano - nascimento
dados['nome'] = nome
dados['idade'] = idade
if ctps > 0:
    dados['ctps'] = ctps
    dados['contratação'] = contrato
    dados['salário'] = salario
    dados['aposentadoria'] = aposentadoria
print(dados)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')