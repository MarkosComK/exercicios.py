l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
A = l * a 
#1 litro de tinta pinta 2m²
print(f'Sua parede tem a dimensão de {l} x {a} e sua área é de {A}')
print(f'Para pintar a parede você precisará de {A/2}l de tinta.')