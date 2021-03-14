matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = somatc = maior = 0
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l} {c}]'))
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
        if matriz[l][c] == matriz[l][2]:
            somatc += matriz[l][c] 
        if matriz[l][c] == matriz[1][c] and matriz[1][c] > maior:
            maior = matriz[1][c]
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma de todos os valores pares digitados é {somap}')
print(f'A soma dos valores da terceira coluna é {somatc}')
print(f'O maior valor da segunda linha é {maior}')
