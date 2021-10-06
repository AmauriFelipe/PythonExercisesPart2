matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_terceira_coluna = 0
maior = 0

for l in range(0,3):

    for c in range(0,3):

        matriz[l][c] = int(input('Digite um valor inteiro para {}, {}: '.format(l, c)))
        matriz[:].clear()

for l in range(0, 3):

    for c in range(0, 3):

        if matriz[l][c] % 2 == 0:

            soma_pares += matriz[c][l]

for l in range(0, 3):

        soma_terceira_coluna += matriz[l][2]

for c in range(0, 3):

    if c == 0:

        maior = matriz[l][c]

    elif matriz[1][c] > maior:

            maior = matriz[l][c]

print('')

for a in range(0,3):

    print(matriz[a])

print('')
print('A soma dos valores pares é {}.'.format(soma_pares))
print('A soma dos valores da terceira coluna é {}.'.format(soma_terceira_coluna))
print('O maior valor da segunda linha é {}.'.format(maior))
