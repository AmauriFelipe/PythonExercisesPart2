colocados = ('América - MG', 'Athletico - PR', 'Atlético - GO',
             'Atlético - MG', 'Bahia', 'Bragantino', 'Ceará',
             'Chapecoense', 'Corinthians', 'Cuiabá', 'Flamengo',
             'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional',
             'Juventude', 'Palmeiras', 'Santos', 'São Paulo',
             'Sport')
alfabeto = ('Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj',
            'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt',
            'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz')

print('Cinco primeiros colocados: {}'.format(colocados[0:5]))
print('')
print('Os 4 últimos colocados: {}'.format(colocados[-1:-5:-1]))
print('')

print('Times em ordem alfabética: ')
for a in range(0, len(colocados)):
    primeiro = colocados[a]
    for b in alfabeto:
        if primeiro[0] in b:
            print(primeiro, end = (', '))

posicao_chapeco = colocados.index('Chapecoense') + 1

print('')
print('')
print('O time da Chapecoense está na {}ª posição.'.format(posicao_chapeco))
