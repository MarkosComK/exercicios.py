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