cont = soma = 0

while True:

    n = int(input('Digite um número:[999 pra parar] '))

    if n == 999:
        break

    cont += 1
    soma += n

print('')
print('Você digitou {} números e sua soma foi {}.'.format(cont, soma))
