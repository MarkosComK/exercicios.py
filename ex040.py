#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO
nota1 = float(input('Digite a 1º nota: '))
nota2 = float(input('Digite a 2º nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'Com notas {nota1} e {nota2} a média é {media}')
    print('O aluno está APROVADO!')
elif media >= 5 < 6.9:
    print(f'Com notas {nota1} e {nota2} a média é {media}')
    print('O aluno está em RECUPERAÇÃO')
elif media < 5:
    print(f'Com notas {nota1} e {nota2} a média é {media}')
    print('O aluno está REPROVADO!')