def maior(* valores):

    maior = 0

    print('Valores passados: ')

    for valor in valores:
        print('{}'.format(valor), end = ' ')
        if valor >= maior:
            maior = valor

    print('\nO maior valor é {}'.format(maior))

maior(2,4,5,67,89,23,3,1,34)
maior(2,6,5,7,1,2)
maior(3)
maior()
