def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    Param n: O número a ser calculado.
    Param show: (opcional) Mostra ou não o cálculo.
    Return: O valor fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='') 
            if c == 1:
                print(' = ', end='')
    print(f'{f}')
    return f

fatorial(5, True)