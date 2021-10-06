maior = 0
opcao = 4
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
while opcao != 5:
    print('')
    print('''[ 1 ] Somar;
[ 2 ] Multiplicar;
[ 3 ] Maior;
[ 4 ] Novos números;
[ 5 ] Sair do programa.''')
    opcao = int(input('Sua escolha: '))
    if opcao == 1:
        print('O resultado da soma entre {} e {} é igual a {}.'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('O produto da multiplicação entre {} e {} é igual a {}.'.format(n1, n2, n1*n2))
    elif opcao == 3:
        if n2 > n1:
            print('O maior valor é {}.'.format(n2))
        elif n2 < n1:
            print('O maior valor é {}.'.format(n1))
        elif n1 == n2:
            print('Não há valor maior. Os dois valores são iguais.')
    elif opcao == 4:
        print('Recomeçando...')
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
    elif opcao == 5:
        print('Ok. Saindo...')
    else:
        print('Opção inválida, tente novamente.')
    print('+='*20)
