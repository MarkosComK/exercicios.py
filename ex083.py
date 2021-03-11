e = str(input('Digite ume expressão: '))
e = e.replace('(', '|')
e = e.replace(')', '|')
v = e.count('|')
if v % 2 == 0:
    print('Expressão válida')
elif v % 2 == 1:
    print('Expressão inválida')