lista = []

while True:
    print('')

    n = int(input('Digite um valor inteiro: '))

    if n not in lista:
        lista.append(n)

        print('Valor adicionado com sucesso.')

    else:
        print('Valor duplicado não adicionado.')

    while True:
        resposta_continuar = str(input('Deseja continuar? [s/n] '))

        if resposta_continuar not in 'NnSs':
            print('Resposta inválida.')
        else:
            break

    if resposta_continuar in 'Nn':
        break

lista.sort()

print('')
print('Ok.')
print('')
print('Sua lista é {}.'.format(lista))
