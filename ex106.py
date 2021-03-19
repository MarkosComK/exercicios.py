from time import sleep

c = {
    '\033[m',         #sem cor
    '\033[0;30;41m'  #vermelho
}

def ajuda(com):
    help(com)

def printl(msg, cor=0):
    print(c[cor], end='')
    print('~'*len(msg))
    print(msg)
    print('~'*len(msg))
    print(c[0], end='')


comando = ''
while True:
    printl('SISTEMA DE AJUDA PYHELP', 1)
    comando = str(input('Digite um comando: '))
    sleep(0.5)
    printl(f'Analisando o comando "{comando}"')
    sleep(1)
    ajuda(comando)
    sleep(1)
    if comando.lower() == 'fim':
        printl('ATÉ LOGO')
        sleep(1)
        break

