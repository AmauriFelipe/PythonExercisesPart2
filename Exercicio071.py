print('Simulador de caixa eletrônico')
print('')

valor = int(input('Digite o valor inteiro a ser sacado: R$'))

total = valor
total_ced = 0
ced = 50

print('')

while True:

    if total >= ced:
        total -= ced
        total_ced += 1

    else:
        if total_ced > 0:
            print('Total de {} cédulas de R${}'.format(total_ced, ced))

        if ced == 50:
            ced = 20

        elif ced == 20:
            ced = 10

        elif ced == 10:
            ced = 1

        total_ced = 0

        if total == 0:
            break

