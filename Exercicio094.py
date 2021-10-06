dados = list()
pessoa = dict()
soma = 0

while True:

    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] '))
        if pessoa['sexo'] in 'FfMm':
            break
        else:
            print('Erro. Digite [F] ou [M].')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']

    dados.append(pessoa.copy())

    while True:
        resposta_continuar = str(input('Deseja continuar? [s/n] '))
        if resposta_continuar in 'SsNn':
            break
        else:
            print('Erro. Responda com [s] ou [n].')
    if resposta_continuar in 'Nn':
        break

media = soma / len(dados)

print('+-' * 20)
print('A) Ao todo temos {} pessoas cadastradas.'.format(len(dados)))
print('B) A média de idade é {} anos.'.format(media))
print('C) As mulheres cadastradas foram: ', end = (''))
for a in dados:
    if a['sexo'] in 'Ff':
        print('{}'.format(a['nome']), end = (' '))
print('\nD) Pessoas com idade acima da média: ', end = (''))
for b in dados:
    if b['idade'] > media:
        print(b['nome'], end = (' '))
