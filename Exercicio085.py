lista = [[], []]

for c in range(0, 7):

    n = int(input('Digite um valor inteiro: '))

    if n % 2 == 0 and n not in lista[0]:

        lista[0].append(n)

    elif n % 2 != 0 and n not in lista[1]:

        lista[1].append(n)

lista[0].sort()
lista[1].sort()

print('')
print('Os valores pares foram: {}'.format(lista[0]))
print('Os valores ímpares foram: {}'.format(lista[1]))
