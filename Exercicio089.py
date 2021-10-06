lista = []

while True:

    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    lista.append([nome, nota1, nota2, media])

    while True:

        resposta_continuar = str(input('Deseja continuar? [s/n] '))

        if resposta_continuar in 'SsNn':

            break

    if resposta_continuar in 'Nn':

        break

print('')
print('Nº   /  Nome       /    Média     ')

for c in range(0, len(lista)):

    print('{:<6}'.format(c), end = (''))
    print('{:<15}'.format(lista[c][0]), end = (''))
    print(lista[c][3])

while True:

    resposta_nota_aluno = int(input('\nVocê deseja ver as notas de que aluno? [999 para parar] '))

    if resposta_nota_aluno == 999:

        break

    for c in range(0, 3):
        print(lista[resposta_nota_aluno][c], end = (', '))

    print('')
