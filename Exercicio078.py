lista_valores = []
index_maior = []
index_menor = []
maior = menor = 0

for a in range(0,5):

    lista_valores.append(int(input('Digite um valor inteiro: ')))

    if a == 0:
        maior = menor = lista_valores[a]
    else:
        if lista_valores[a] > maior:
            maior = lista_valores[a]
        elif lista_valores[a] < menor:
            menor = lista_valores[a]

for b in range(0, len(lista_valores)):
    if lista_valores[b] == maior:
        index_maior.append(b)
    elif lista_valores[b] == menor:
        index_menor.append(b)

print('')

if len(index_maior) == 1:
    print('O maior valor foi {} que apareceu na posição {}'.format(maior, index_maior))
else:
    print('O maior valor foi {} que apareceu nas posições {}'.format(maior, index_maior))

if len(index_menor) == 1:
    print('O menor valor foi {} que apareceu na posição {}.'.format(menor, index_menor))
else:
    print('O menor valor foi {} que apareceu nas posições {}.'.format(menor, index_menor))
