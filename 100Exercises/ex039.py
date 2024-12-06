#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date, datetime
ano = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {atual}')
if idade >= 18:
    print(f'Você já devia ter se alistado há {idade - 18} anos')
    print(f'Seu alistamento foi em {atual - (idade - 18)}')
elif idade == 17:
    print(f'você deve se alistar esse ano!')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos pro seu alistamento')