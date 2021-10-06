print('Gerador de P.A.')
n1 = int(input('Primeiro termo inteiro: '))
r = int(input('Razão inteira: '))
n = int(input('Número de termos: '))
termo = n1
c = 1
while c <= n:
    print('{}; '.format(termo), end = (''))
    termo += r
    c += 1
print('Fim.')