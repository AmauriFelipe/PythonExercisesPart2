valores = (int(input('Digite um valor inteiro: ')),
           int(input('Digite outro valor inteiro: ')),
           int(input('Digite outro valor inteiro: ')),
           int(input('Digite o último valor inteiro: ')))

print('')

if 9 in valores:
    print('O número 9 apareceu {} vezes.'.format(valores.count(9)))
else:
    print('O valor 9 não foi digitado.')

print('')

if 3 in valores:
    print('O número 3 apareceu na posição {}.'.format(valores.index(3) + 1))
else:
    print('O valor 3 não foi digitado.')

print('')

print('Os valores pares digitados foram: ', end = (''))
for o in valores:
    if o % 2 == 0:
        print(o, end = (''))
