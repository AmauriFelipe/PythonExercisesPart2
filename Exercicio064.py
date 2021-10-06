n = int(input('Digite alguns valores inteiros. Pra parar digite 999. '))
cont = 0
s = n

while n != 999:
    cont += 1
    n = int(input(''))
    s += n
s1 = s - 999
print('')
print('Você digitou {} números.'.format(cont))
print('Sua soma é {}.'.format(s1))

