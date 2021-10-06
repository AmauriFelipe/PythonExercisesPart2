resposta = str('s')
contador = maior = menor = soma = 0

while resposta in 'Ss':
    n = int(input('Digite um valor inteiro: '))
    contador += 1
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
    resposta = str(input('Deseja continuar? [s/n] '))

media = soma / contador

print('')
print('Você digitou {} números.'.format(contador))
print('A média entre eles é {:.2f}.'.format(media))
print('O maior valor foi {}.'.format(maior))
print('O menor valor foi {}.'.format(menor))