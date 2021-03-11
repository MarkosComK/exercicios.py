p = float(input('Qual o preço do produto? '))
pcd = p - (p / 100 * 5)
print(f'O produto que custava {p}R$, na promoção com desconto de 5% \n vai custar {pcd:.2f}R$')