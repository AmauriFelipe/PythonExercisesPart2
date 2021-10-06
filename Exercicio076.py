produtos_e_precos = ('Lápis', 1.23,
                     'Borracha', 0.78,
                     'Apontador', 3,
                     'Pacote com 50 folhas A4', 5.30,
                     'Estojo', 7,
                     'Caneta', 2,
                     'Compasso', 3,
                     'Caderno 100 folhas', 7)

print('=' * 40)

for posicao in range(0, len(produtos_e_precos)):
    if posicao % 2 == 0:
        print('{:.<30}'.format(produtos_e_precos[posicao]), end = (''))
    else:
        print('R${:>7.2f}'.format(produtos_e_precos[posicao]))

print('=' * 40)
