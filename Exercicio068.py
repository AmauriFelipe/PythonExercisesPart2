from random import randint

ncomp = randint(1, 10)
contador = 0

print('Vamos brincar.')

while True:

    njog = int(input('Digite um valor inteiro: '))
    escolha = int(input('Escolha par ou ímpar: (1 para par ou 2 para ímpar) '))

    soma = njog + ncomp

    print('')
    print('Eu joguei {}. O total é {}.'.format(ncomp, soma))
    print('')

    if escolha == 1:
        if soma % 2 == 0:
            contador +=1
            print('Você escolheu par. Você ganhou!')
        else:
            print('Você escolheu par. Você perdeu.')
            break
    if escolha == 2:
        if soma % 2 == 0:
            print('Você escolheu ímpar. Você perdeu.')
            break
        else:
            contador += 1
            print('Você escolheu ímpar. Você ganhou.')

print('')
print('Você ganhou {} vezes.'.format(contador))
