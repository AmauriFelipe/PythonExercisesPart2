matriz = dict()
matriz_esc = dict()
respostas = dict()

respostas['num_lin'] = int(input('Digite o número de linhas da matriz: '))
respostas['num_col'] = int(input('Digite o número de colunas da matriz: '))

for a in range(1, respostas['num_lin'] + 1):
    for b in range(1, respostas['num_col'] + 1):
        matriz['M({} {})'.format(a, b)] = int(input('Digite o valor inteiro para {}: '.format('M({} {})'.format(a, b))))

print('')
print('Matriz M:')
print('')

for a in range(1, respostas['num_lin'] + 1):
    for b in range(1, respostas['num_col'] + 1):
        print('{} '.format(matriz['M({} {})'.format(a, b)]), end = (''))
    print('\n', end = (''))

print('')
print('Eliminação gaussiana:')
print('')

if matriz['M(1 1)'] != 0:
    for c in range(1, respostas['num_col'] + 1):
        matriz_esc = matriz['M(1 {})'.format(c)] * (matriz['M(2 {})'.format(c)] / matriz['M(1 1)'])
