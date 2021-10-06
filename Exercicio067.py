while True:

    contador = 0

    n = int(input('Quer ver a tabuada de que número? (valor negativo pra parar) '))

    if n < 0:
        break

    print('')
    print('+-'*10)
    print('')

    for c in range(1, 10+1):
        contador += 1
        produto = n * contador
        print('{} x {} = {}'.format(n, contador, produto))

    print('')
    print('+='*10)
    print('')

print('')
print('Programa encerrado.')
