from random import randint

valores_sorteados = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: {}'.format(valores_sorteados))
print('')
print('O maior valor foi {}.'.format(max(valores_sorteados)))
print('O menor valor foi {}.'.format(min(valores_sorteados)))
