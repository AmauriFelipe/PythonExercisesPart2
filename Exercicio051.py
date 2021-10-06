a1 = float(input('Digite o primeiro termo da progressão: '))
r = float(input('Digite a razão da progressão: '))
print(' ')
print('Primeiro ao décimo termos da progressão: ')
for p in range(1, 10+1):
    an = a1 + r * (p - 1)
    print(an, end=(', '))
print('fim.')