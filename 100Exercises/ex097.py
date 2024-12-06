# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def mensagem(txt):
    v = len(txt) + 4
    print('~' * v)
    print(' ', txt)
    print('~' * v)


mensagem('Olá, mundo!')
mensagem('Exercício concluido')
mensagem('Curso em Vídeo')