def fatorial(a, show=bool):
    '''
    => Calcula o fatorial de um número.

    fatorial(a, show = bool)

    a = Valor a ser calculado o fatorial
    show = Mostra o cálculo.
    '''

    print('Fatorial de {}'.format(a))

    r = 1

    for c in range(a, 0, -1):
        r *= c

        if show == True:
            print(c, end = '')

        if c != 1 and show == True:
            print(' x ', end = '')

    print(' = ', end = '')

    return r


print(fatorial(4, show = True))
