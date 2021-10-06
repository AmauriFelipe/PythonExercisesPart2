lista = []

while True:

    print('')

    lista.append(int(input('Digite um valor inteiro: ')))

    while True:
        resposta_continuar = str(input('Deseja continuar? [s/n] '))

        if resposta_continuar in 'SsNn':
            break

    if resposta_continuar in 'Nn':
        break

print('')
print('Você digitou {} números.'.format(len(lista)))
print('')

lista.sort(reverse = True)

print('Os valores em ordem decrescente são {}.'.format(lista))
print('')

if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
