Frase = str(input('Digite uma frase: ')).replace(' ', '')
print(Frase[::-1].upper())
if Frase == Frase[::-1]:
    print('É um PALÍNDROMO!')
else:
    print('NÃO é um PALÍNDROMO!')
