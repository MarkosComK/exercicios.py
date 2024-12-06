#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).upper().strip()
la = frase.count('A')
frase.replace(' ', '')
PrimeiraPosicao = frase.find('A')+1
UltimaPosicao = frase.rfind('A')
print(f'A letra "A" aparece {la} vezes')
print(f'A primeira letra "A" aparece na posição {PrimeiraPosicao}')
print(f'A última letra "A" aparece na posição {UltimaPosicao}')
