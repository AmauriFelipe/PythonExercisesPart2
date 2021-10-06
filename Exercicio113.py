def leiaInt(msg):
    while True:
        try:
            n = int(input(msg).strip())

        except (ValueError, TypeError):
            print('\033[1;31;mErro. Digite um número inteiro válido!\033[m')

            continue

        except (KeyboardInterrupt):
            print('\033[1;31;mEntrada de dados interrompitda peo usuário.\033[m')

            return 0

        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.').strip())

        except (ValueError, TypeError):
            print('\033[1;31;mErro. Digite um número real válido!\033[m')

            continue

        except (KeyboardInterrupt):
            print('\033[1;31;mEntrada de dados interrompitda peo usuário.\033[m')

            return 0

        else:
            return n


def comandodoexercicio():
    n1 = leiaInt('Digite um número inteiro: ')
    n2 = leiaFloat('Digite um número real: ')

    print('Você digitou o valor inteiro {} e o valor real {}.'.format(n1, n2))
