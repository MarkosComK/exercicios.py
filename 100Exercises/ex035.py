#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-='*12)
print('ANALISADOR DE TRÍANGULOS')
print('-='*12)
s1 = float(input('Digite o 1º seguimento: '))
s2 = float(input('Digite o 2º seguimento: '))
s3 = float(input('Digite o 3º seguimento: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1 and s2 + s1 > s3:
    print('Os seguimentos digitados podem formar um tríangulo')
else:
    print('Os seguimentos digitados não podem formar um tríangulo')