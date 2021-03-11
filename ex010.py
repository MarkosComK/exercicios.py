n = float(input('Digite quanto você tem na carteira: '))
d = n / 5.65
if d <= 1:
    print(f'{n} R$ compram {d:.0f} Dólar.')
else:
    print(f'{n} R$ compram {d:.2f} Dólares.')