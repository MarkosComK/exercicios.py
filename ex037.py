#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input('Digite um número inteiro: '))
print('-='*19)
print('Escolha uma das bases para conversão')
print('-='*19)
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')
o = int(input('Sua opção: '))
if o == 1:
    print(f'O número digitado convertido para binário é {bin(numero)[2:]}')
elif o == 2:
    print(f'O número digitado convertido para octal é {oct(numero)[2:]}')
elif o == 3:
    print(f'O número digitado convertido para hexadecimal é {hex(numero)[2:]}')
elif 0 != 1 or 2 or 3:
    print('Opção selecionada INVÁLIDA')