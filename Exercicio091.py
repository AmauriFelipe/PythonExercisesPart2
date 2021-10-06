from random import randint

sorteados = {}

for a in range(0, 4):

    sorteados['jogador {}'.format(a + 1)] = randint(1, 6)

for b, c in sorteados.items():

    print('{} ficou com {}'.format(b, c))

ranking = sorted(sorteados.items(), key=itemgetter(1) reverse = True)

for i, v in enumerate(ranking):
    print('{}º lugar: {} com {} pontos.'.format(i + 1, v[0], v[1]))
