extenso = ('zero', 'um', 'dois','três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'desessete', 'dezoito', 'dezenove','vinte')
opcao = int(input('Digite um número entre 0 e 20: '))
while opcao > 20 or opcao < 0:
    opcao = int(input('Opção inválida. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {extenso[opcao]}')