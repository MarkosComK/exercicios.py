from random import randint
from time import sleep
import os


# Gerar um conjunto de 6 números aleatórios e distintos, com valores entre n1 e n2 (inclusive).
def cartela(n1=1, n2=10):
    numeros = []

    while (len(numeros) < n2):
        num = randint(1, 60)
        if (contido(num, numeros) == False):
            numeros.append(num)

    return numeros

# Verificar se um número está contigo em uma lista.
def contido(n, lista):
    if (n in lista):
        return True
    else:
        return False

# Verificar quantos números da lista 1(l1) estão contidos na lista 2 (l2)
def verificar(l1, l2):
    qtde = 0
    for i in range(len(l1)):
        if (contido(l1[i], l2) == True):
            qtde += 1
    return qtde

# Inserir um número em uma lista, apenas se este número não estiver
# contigo na lista.
def inserir(lista):
    valor = randint(1, 10)
    if (contido(valor, lista) == False):
        lista.append(valor)


# trocar os valores de n1 e n2
def trocar(n1, n2):
    n1, n2 = n2, n1

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def quantidadeCartelas(v):
    n1 = 0
    todasCartelas = []
    while n1 < v:
        todasCartelas.append(cartela())
        n1 += 1
    return todasCartelas


##não está em uso
def printCartelas():
    i = 0
    while i < len(cartelas):
        sleep(0.5)
        print(cartelas[i])
        i += 1

#cria uma lista para salvar a pontuação de cada jogador

def adicionaJogador(jogadores):
    c = 0
    listaJogadores = []
    while c < jogadores:
        listaJogadores.append([])
        c += 1
    return listaJogadores

#Pergunta quantos jogadores serão... A quantidade de jogadores é a quantidade de cartelas sorteadas
jogadores = int(input('Qual a quantidade de jogadores?'))
listaJogadores = adicionaJogador(jogadores)

sleep(0.5)

#Salva cada certela dentro da variável ~cartelas~ abaixo:
cartelas = quantidadeCartelas(jogadores)



listaNumerosSorteados = []
listaVencedora = []

while True:
    limpar()
    numeroSorteados = []
    numeroSorteado = randint(1, 60)
    listaNumerosSorteados.append(numeroSorteado)
    numeroSorteados.append(numeroSorteado)
    print('')
    print(f'Número sorteado {numeroSorteado}')
    parar = False


    ### Marca a pontuação do jogador
    con = 0
    while con < len(listaJogadores):
        listaJogadores[con].append(verificar(cartelas[con], numeroSorteados))
        con += 1

    ### printa as cartelas uma abaixo da outra junto com sua respectiva pontuação
    i = 0
    while i < len(cartelas):
        r = i+1
        print(f'Jogador {r:>2} {cartelas[i]} pontos: {sum(listaJogadores[i]):>2}')
        i += 1


    contador = 0
    while contador < len(listaJogadores):
        if sum(listaJogadores[contador]) == 10:
            listaVencedora = cartelas[contador]
            print('Temos um vencedor!')
            parar = True
            break
        else:
            contador += 1
    if parar == True:
        break
    questao = str(input('Pressione Enter para sortear um novo número ou digite F para encerrar: ')).upper()
    if questao == 'F':
        parar = True
    if parar == True:
        break
    limpar()

print('A lista vencedora foi: ')
print(listaVencedora)
print('Os números sorteados foram: ')
print(listaNumerosSorteados)
while True:
    fechar = False
    saida = str(input('Deseja sair do programa? [S/N]')).upper()
    if saida in  'sS':
        fechar = True
    if fechar == True:
        break
    