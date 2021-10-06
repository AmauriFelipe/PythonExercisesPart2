numero_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                      'seis', 'sete', 'oito',
                      'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
                      'quinze', 'dezesseis', 'dezessete', 'dezoito',
                      'dezenove', 'vinte')

while True:
    resposta_numero = int(input('Digite um número entre 0 e 20: '))

    if 0 <= resposta_numero <= len(numero_por_extenso):
        break

    print('Resposta incorreta. Tente novamente.')
    print('')

print('')
print('Você digitou o número {}.'.format(numero_por_extenso[resposta_numero]))
