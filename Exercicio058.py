from random import randint
ncomp = randint(1, 10)
njog =int(input('Tente adivinhar o número inteiro entre 1 e 10 em que eu estou pensando: '))
cont = 1
while njog != ncomp:
    cont += 1
    if njog < ncomp:
        njog = int(input('Mais... tente novamente: '))
    elif njog > ncomp:
        njog = int(input('Menos... tente novamente: '))
print('')
print('Você acertou! Foram no total {} tentativas até acertar.'.format(cont))