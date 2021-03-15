#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes
print('-='*12)
print('ANALISADOR DE TRÍANGULOS')
print('-='*12)
s1 = float(input('Digite o 1º seguimento: '))
s2 = float(input('Digite o 2º seguimento: '))
s3 = float(input('Digite o 3º seguimento: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1 and s2 + s1 > s3:
    print('Os seguimentos digitados podem formar um tríangulo')
    if s1 == s2 == s3:
        print("O Tríangulo formado é EQUILÁTERO")
    if s1 != s2 != s3 != s1:
        print('O Tríangulo formado é ESCALENO')
    if s1 == s2 and s1 != s3 or s2 == s3 and s2 != s1 or s1 == s3 and s3 != s2:
        print('O Tríangulo formado é ISÓSCELES')
else:
    print('Os seguimentos digitados não podem formar um tríangulo')