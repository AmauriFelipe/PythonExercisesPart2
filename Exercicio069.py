contador_idade = 0
contador_homem = 0
contador_mulher_menor_de_20 = 0

while True:

    print('')
    while True:
        idade = int(input('Qual é a idade dessa pessoa? '))
        if idade in range(0,200):
            break
    while True:
        sexo = str(input('Qual é o sexo dessa pessoa? [M/F] ')).strip()
        if sexo in 'MmFf':
            break

    print('')

    if idade > 18:
        contador_idade += 1
    if sexo in 'Mm':
        contador_homem += 1
    if sexo in 'Ff' and idade < 20:
        contador_mulher_menor_de_20 += 1

    while True:
        respostacontinuar = str(input('Quer continuar? [s/n] ')).strip()
        if respostacontinuar in 'SsNn':
            break

    if respostacontinuar in 'Nn':
        break

print('+-'*20)

if contador_idade == 0:
    print('Não foram registrados maiores de idade.')
else:
    print('Foram registrados {} maiores de 18 anos.'.format(contador_idade))

print('')

if contador_homem == 0:
    print('Não foram registrados homens.')
else:
    print('Foram registrados {} pessoas do sexo masculino.'.format(contador_homem))

print('')

if contador_mulher_menor_de_20 == 0:
    print('Não foram registradas pessoas do sexo feminino menores de 20 anos.')
else:
    print('Foram registradas {} pessoas do sexo feminino menores de 20 anos.'.format(contador_mulher_menor_de_20))
