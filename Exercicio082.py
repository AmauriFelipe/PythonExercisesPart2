lista = list()
lista_pares = list()
lista_impares = list()

while True:
    print('')

    n = int(input('Digite um número inteiro: '))

    lista.append(n)

    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)

    while True:
        resposta_continuar = str(input('Deseja continuar? [s/n] '))

        if resposta_continuar in 'SsNn':
            break

    if resposta_continuar in 'Nn':
        break

print('')
print('Sua lista é {}.'.format(lista))
print('Os números pares foram {}.'.format(lista_pares))
print('Os números ímpares foram {}.'.format(lista_impares))
