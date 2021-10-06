def ajuda(x):
    print('\033[0;30;42mAjuda interativa do Python\033[m')
    help(x)
    print('\033[0;30;42mFim\033[m')


#Programa Principal

while True:

    print('')

    resp = str(input('Função ou biblioteca: [999 pra finalizar] '))

    if resp == '999':
        break
    else:
        ajuda(resp)
