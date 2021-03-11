from datetime import date
print('-='*19)
print('CATEGORIAS DE PESO ADULTO/MASTER JIU-JITSU')
print('-='*19)
#ano = int(input('Digite o ano de nascimento: '))
peso = float(input('Digite o seu peso: '))
#idade = AnoAtual - ano
#AnoAtual = date.today().year
print(AnoAtual)
if peso <= 57.5:
    print('O atleta pertence a categoria GALO (até 57.5 KG)')
elif peso < 64:
    print('O atleta pertence a categoria PLUMA (até 64.0 KG)')
elif peso < 70:
    print('O atleta pertence a categoria PENA (até 70.0 KG)')
elif peso < 76:
    print('O atleta pertence a categoria LEVE (até 76.0 KG)')
elif peso < 82.3:
    print('O atleta pertence a categoria MÉDIO (até 82.3 KG)')
elif peso < 88.3:
    print('O atleta pertence a categoria MEIO-PESADO (até 88.3 KG)')
elif peso < 94.3:
    print('O atleta pertence a categoria PESADO (até 94.3 KG)')
elif peso < 100.5:
    print('O atleta pertence a categoria SUPER PESADO (até 100.5 KG)')
