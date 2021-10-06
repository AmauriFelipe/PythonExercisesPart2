jogo = dict()
partidas = list()
jogo['jogador'] = str(input('nome do jogador: '))
tot = int(input('Quantas partidas {} jogou? '.format(jogo['jogador'])))

for a in range(0, tot):

    partidas.append(int(input('Quantos gols ele fez na {}ª partida? '.format(a + 1))))

jogo['gols'] = partidas[:]
jogo['totalgols'] = sum(partidas)

print('+-' * 20)
print(jogo)
print('+=' * 20)

for b, c in jogo.items():

    print('O campo {} tem o valor {}.'.format(b, c))

print('+=' * 20)
print('O jogador {} jogou {} partidas.'.format(jogo['jogador'], tot))
print('+-' * 20)

for d, e in enumerate(jogo['gols']):

    print('    > Na {}ª partida, {} fez {} gols.'.format(d + 1, jogo['jogador'], e))

print('')
print('{} fez um total de {} gols.'.format(jogo['jogador'], jogo['totalgols']))
