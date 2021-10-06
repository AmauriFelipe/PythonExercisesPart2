print('Gerador de P.A. v3.0')
print('+='*15)
n1 = int(input('Primeiro termo inteiro: '))
r = int(input('Razão inteira: '))
n = int(input('Número de termos desejado: '))
c = 0
termo = n1
while n != 0 and c < n:
    print('{}; '.format(termo), end = (''))
    termo += r
    c += 1
    if c == n:
        print(' pausa')
        n = int(input('Deseja mais quantos termos? '))
        c = 0
print('Fim.')
