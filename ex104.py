def leiaInt(msg):
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('ERRO: digite um número inteiro válido')     
    return valor


n = leiaInt('Digite um número: ')
print(f'você acaba de digitar o número {n}')