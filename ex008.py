#Escreva um programa que leia o valor em metros e o exiba convertido em centímetros e milímetros.
v = float(input('Uma distância em métros: '))
print(f'A medida de {v}m corresponde a:')
print(f'{v/1000} km')
print(f'{v/100} hm')
print(f'{v/10} dam')
print(f'{v/0.1} dm')
print(f'{v/0.01} cm')
print(f'{v/0.001} mm')