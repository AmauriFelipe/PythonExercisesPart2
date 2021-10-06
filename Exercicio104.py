def leiaInt(txt = 0):
    teste = False

    while teste == False:
        n = str(input(txt))

        if n.isnumeric():
            valor = int(n)
            teste = True
        else:
            print('\033[1;31;mErro. Digite um número inteiro válido.\033[m')

        if teste == True:
            break

    return valor


n = leiaInt('Digite um número: ')
print('Você acabou de digitar o número {}'.format(n))
