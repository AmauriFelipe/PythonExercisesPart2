lista = []
jogador = {}
partidas = []

while True:

    print('')

    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input('{} jogou em quantas partidas? '.format(jogador['nome'])))

    partidas.clear()

    for a in range(1, tot + 1):
        partidas.append(int(input('     {} fez quantos gols na {} partida? '.format(jogador['nome'], a))))

    jogador['gols'] = partidas[:]

    lista.append(jogador.copy())

    while True:
        resposta_continuar = str(input('Deseja continuar? [s/n]'))

        if resposta_continuar in 'SsNn':
            break

    if resposta_continuar in 'Nn':
        break

print('+='* 20)
print('Código / Nome       / Gols           / Total')

for b in range(0, len(lista)):
    print('{:<9}{:<13}{}           {}'.format(b, lista[b]['nome'], lista[b]['gols'], sum(lista[b]['gols'])))

while True:
    busca = int(input('Exibir dados de qual jogados? [999 para finalizar] '))

    if busca == 999:
        break

    elif busca >= len(lista):
        print('Erro. Não existe jogador com esse código.')

    else:
        print('')
        print('Levantamento do jogador {}:'.format(lista[busca]['nome']))

        for c, d in enumerate(lista[busca]['gols']):
            print('Na partida {} ele fez {} gols.'.format(c, d))
