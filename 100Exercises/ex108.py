from ex108 import moeda

v = float(input("Digite o preço: R$ "))
print(f'A metade de {moeda.moeda(v)} é {moeda.moeda(moeda.metade(v))}')
print(f'O dobro de {moeda.moeda(v)} é {moeda.moeda(moeda.dobro(v))}')
print(f'Aumentando em 10%, temos {moeda.moeda(moeda.aumentar(v, 10))}')
print(f'Reduzindo em 13%, temos {moeda.moeda(moeda.diminuir(v, 13))}')