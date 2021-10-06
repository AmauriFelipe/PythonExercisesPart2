def contador(inicio, fim, passo):

    c = inicio

    print('\n')
    print('Contagem de {} até {} de {} em {}:'.format(inicio, fim, passo, passo))

    if inicio <= fim:

        while c <= fim:
            print(c, end = ' ')
            c += passo

    else:
        while c >= fim:
            print(c, end = ' ')
            c -= passo


contador(0, 10, 1)
contador(10, 0, 2)

print('\n')

contador(int(input('Digite o valor de início: ')),
         int(input('Digite o valor final: ')),
         int(input('Digite o passo: ')))
