Midade = 0
ContadorFeminino = 0
MaisVelho = 0
NomeMaisVelho = 'vazio'
for p in range(1, 5):
    print('-='*19)
    print(f'            {p}º PESSOA')
    print('-='*19)
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    sex = str(input('Sexo[M/F]: ')).upper().strip()
    Midade += age
    if sex == 'F' and age < 20:
        ContadorFeminino += 1
    if sex == 'M' and age > MaisVelho:
        MaisVelho = age
        NomeMaisVelho = name
print(f'A média de idade do grupo é de {Midade/4} anos')
print(f'Ao todo são {ContadorFeminino} mulheres com menos de 20 anos')
print(f'O homem mais velho tem {MaisVelho} anos e se chama {NomeMaisVelho}')