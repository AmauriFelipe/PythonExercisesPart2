cadastrados = []
dados = []
maior_peso = menor_peso = 0
lista_maior_peso = []
lista_menor_peso = []

while True:

    print('')
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(cadastrados) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]

    cadastrados.append(dados[:])
    dados.clear()

    while True:

        resposta_continuar = str(input('Deseja continuar? [s/n] '))

        if resposta_continuar in 'SsNn':
            break

    if resposta_continuar in 'Nn':
        break

for pessoas in cadastrados:
    if pessoas[1] == maior:
        lista_maior_peso.append(pessoas[0])
    elif pessoas[1] == menor:
        lista_menor_peso.append(pessoas[0])

print('')
print('Os cadastrados foram {}.'.format(cadastrados))
print('Você cadastrou {} pessoas.'.format(len(cadastrados)))
print('As pessoas de maior peso são {}.'.format(lista_maior_peso))
print('As pessoas de menor peso sao {}.'.format(lista_menor_peso))
