a = 0
b = 1
cont = 0

n = int(input('Você deseja ver quantos termos da sequência de Fibonnacci? '))
while n != 0:
    print('{}, {}, '.format(a, b), end = (''))
    cont = 0
    while cont < n:
        cont += 1
        c = a + b
        print(c, end = (', '))
        a = b
        b = c
    n = int(input('Deseja ver mais quantos termos? '))
print('')
print('Fim.')