def ficha(nome = 0, gols = 0):
    if nome == '':
        nome = '<desconhecido>'

    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = str('<valor desconhecido>')

    print('O jogador {} fez {} gols'.format(nome, gols))


nome = str(input('Digite o nome do jogador: '))
gols = (input('Digite o número de gols que ele fez: '))

ficha(nome, gols)
