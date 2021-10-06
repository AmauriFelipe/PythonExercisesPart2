from random import randint

lista_jogos = []
jogos = []

print('Mega-sena')
print('')

numero_jogos = int(input('Você quer que eu sorteie quantos jogos? '))
print('')

for c in range(0, numero_jogos):

    lista_jogos.append(jogos)

    for d in range(0, 6):

        n = randint(1, 60)

        if n not in lista_jogos[c]:

            lista_jogos[c].append(n)

        else:

            n = randint(1, 60)

            lista_jogos[c].append(n)

    print('Jogo {}: {}'.format(c + 1, lista_jogos[c]))

    lista_jogos[c - 1].clear()
