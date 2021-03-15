#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
e = str(input('Digite ume expressão: '))
e = e.replace('(', '|')
e = e.replace(')', '|')
v = e.count('|')
if v % 2 == 0:
    print('Expressão válida')
elif v % 2 == 1:
    print('Expressão inválida')